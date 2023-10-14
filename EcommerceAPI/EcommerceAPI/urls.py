
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from product import views
router=DefaultRouter()
router.register("category", views.CategoryView, basename='product-category')
router.register("brand", views.BrandView, basename='product-brand')
router.register("product", views.ProductView, basename='product')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/doc/", SpectacularSwaggerView.as_view(url_name="schema"), name="schema-doc")
]

