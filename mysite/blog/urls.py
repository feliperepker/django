from django.urls import path
import views
urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]