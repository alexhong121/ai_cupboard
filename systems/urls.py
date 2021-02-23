from django.urls import path
from systems import views

urlpatterns = [
    path('configuration', views.Configlist.as_view()),                 #Configuration list
    path('configuration/<int:pk>', views.ConfigDetail.as_view()),     #Configuration Detail
    path('information',views.Informationlist.as_view()),                 #information list
    path('information/<int:pk>', views.InformationDetail.as_view()),      #information Detail
]