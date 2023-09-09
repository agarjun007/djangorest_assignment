from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['put'])
    def toggle_status(self, request, pk=None):
        product = self.get_object()
        if product.active and (timezone.now() - product.created_at).days > 60:
            product.active = False
            product.save()
            return Response({'message': 'Product Deactivated'}, status=status.HTTP_200_OK)
        elif not product.active:
            product.active = True
            product.save()
            return Response({'message': 'Product activated'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Product cannot be Deactivated as it was registered within 2 months.'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Check if the product can be updated based on the active/inactive condition
        if not request.data.get('active') and (timezone.now() - instance.created_at).days < 60:
            return Response({'message': 'Product cannot be deactivated as it was registered within 2 months'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.deleted_at = timezone.now()
        product.save()
        return Response({'message': 'Product deleted'}, status=status.HTTP_200_OK)
