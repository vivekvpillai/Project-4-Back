from django.urls import path
from . import views

urlpatterns = [
    path('api/foods', views.FoodList.as_view(), name='food_list'),
    path('api/foods/<int:pk>', views.FoodDetail.as_view(), name='food_detail')
]