import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_payment_intent(amount, currency='usd'):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert to cents
            currency=currency,
        )
        return intent
    except stripe.StripeError as e:
            # Log the error and handle it appropriately
            print(f"Stripe error: {str(e)}")
            raise

def confirm_stripe_payment(payment_intent_id):
    try:
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return intent.status == 'succeeded'
    except stripe.StripeError as e:
        # Log the error and handle it appropriately
        print(f"Stripe error: {str(e)}")
        raise