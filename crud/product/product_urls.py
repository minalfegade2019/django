from django.urls import path
from product import views
urlpatterns = [
    path('show/', views.show),
    path('add/', views.add),
    path('update/<product_id>', views.update),
    path('delete/<product_id>', views.delete),
]