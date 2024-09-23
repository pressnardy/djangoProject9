from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
	path("", views.index, name="index"),
	path('register', views.register, name="register"),
	path('search', views.search_view, name="search"),
	path('client/<int:client_id>/', views.client_details, name='client_details'),
	path('client/<int:client_id>/edit/', views.edit_client, name='edit_client'),
	path('client/<pk>/delete/', views.delete_client, name='delete'),
]

