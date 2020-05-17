from django.urls import path
from .views import create_form , list_view , detail_view , update_view, delete_view, tagged
urlpatterns = [
	path('' , list_view, name='list'),
	path('detail/<str:slug>/' , detail_view , name='detail'),
	path('create/' , create_form , name='create'),
	path('edit/<str:slug>/' , update_view , name='edit'),
	path('tag/<str:slug>/' , tagged , name='tagged'),

	path('delete/<str:slug>/' , delete_view , name='delete'),
]