from django.urls import path
from .import views
app_name='post'
urlpatterns = [
    path('', views.post,name='post'),
    path('<int:id>', views.post_details,name='post_details'),
]
