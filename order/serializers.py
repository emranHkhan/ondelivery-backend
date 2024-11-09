from rest_framework import serializers
from .models import Order, OrderItem
from foodItem.models import FoodItem
from foodItem.serializers import FoodItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    food_item_details = FoodItemSerializer(source='food_item', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['food_item', 'food_item_details', 'quantity', 'price']
        read_only_fields = ['price']  
        extra_kwargs = {
            'food_item': {'write_only': True}
        }

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'status', 'items', 'created_at']
        read_only_fields = ['status', 'total_amount']  

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        total_amount = 0
        for item_data in items_data:
            food_item_id = item_data['food_item']
            food_item = FoodItem.objects.get(id=food_item_id)
            quantity = item_data['quantity']
            price = food_item.price * quantity
            total_amount += price
            
            OrderItem.objects.create(
                order=order,
                food_item=food_item,
                quantity=quantity,
                price=price
            )
        
        order.total_amount = total_amount
        order.save()
        
        return order
