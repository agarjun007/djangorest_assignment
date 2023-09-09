from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomerViewSet, ProductViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/<int:pk>/toggle-status/', ProductViewSet.as_view({'put': 'toggle_status'}), name='product-toggle-status'),

]
