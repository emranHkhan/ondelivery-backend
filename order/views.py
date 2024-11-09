from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import stripe
from .models import Order, OrderItem
from .serializers import OrderSerializer
from .utils import confirm_stripe_payment
from rest_framework import generics
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
from foodItem.models import FoodItem
class ConfirmPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        order_id = request.data.get('order_id')
        payment_intent_id = request.data.get('payment_intent_id')
        
        if not order_id or not payment_intent_id:
            return Response(
                {'error': 'Missing order_id or payment_intent_id'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            order = get_object_or_404(
                Order, 
                id=order_id, 
                user=request.user,
                status='PENDING'
            )
            
            # Verify payment status with Stripe
            payment_status = confirm_stripe_payment(payment_intent_id)
            
            if payment_status.get('status') == 'succeeded':
                order.status = 'PAID'
                order.save()
                
                serializer = OrderSerializer(order)
                return Response({
                    'message': 'Payment successful',
                    'order': serializer.data
                })
            else:
                order.status = 'FAILED'
                order.save()
                return Response(
                    {
                        'error': 'Payment failed',
                        'details': payment_status.get('error_message', 'Unknown error')
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except stripe.StripeError as e:
            # Log the error
            print(f"Stripe error: {str(e)}")
            return Response(
                {'error': 'Payment processing error'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Log the error
            print(f"Unexpected error: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CreateOrderView(APIView):
    def post(self, request):
        user = request.user
        items_data = request.data.get('items', [])
        total_amount = request.data.get('total_amount', 0)
        first_name = request.data.get('firstName')
        last_name = request.data.get('lastName')
        email = request.data.get('email')
        phone = request.data.get('phone')
        street = request.data.get('street')
        city = request.data.get('city')
        state = request.data.get('state')
        zip_code = request.data.get('zipCode')
        country = request.data.get('country')

        try:
                order = Order.objects.create(
                    user=user,
                    total_amount=total_amount,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    street=street,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    country=country
                )

                for item_data in items_data:
                    food_item_id = item_data.get('food_item')
                    quantity = item_data.get('quantity', 1)
                    
                    if not food_item_id or not quantity:
                        raise ValueError("Each item must have a 'food_item' ID and 'quantity'.")
                    
                    try:
                        food_item = FoodItem.objects.get(id=food_item_id)
                    except FoodItem.DoesNotExist:
                        raise ValueError(f"FoodItem with id {food_item_id} does not exist.")

                    OrderItem.objects.create(order=order, food_item=food_item, quantity=quantity, price=food_item.price * quantity)

                try:
                    intent = stripe.PaymentIntent.create(
                        amount=int(total_amount * 100),  
                        currency='usd',
                        metadata={'order_id': order.id}
                    )
                    return Response({'client_secret': intent.client_secret, 'order_id': order.id}, status=status.HTTP_201_CREATED)
                except Exception as e:
                    raise ValueError(f"Error creating Stripe PaymentIntent: {str(e)}")
        
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def confirm_stripe_payment(payment_intent_id):
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return {'status': payment_intent.status, 'error_message': None}  
    except stripe.error.StripeError as e:
        return {'status': 'failed', 'error_message': str(e)}
    except Exception as e:
        return {'status': 'error', 'error_message': str(e)}


class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)