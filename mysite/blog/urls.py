from django.urls import path
import views
urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path("<slug:slug>/", views.PostDetail.as_view(), name= 'post_detail')
]