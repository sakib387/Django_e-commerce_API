
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product import views
router=DefaultRouter()
router.register("category", views.CategoryView, basename='product-category')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(router.urls))
]
