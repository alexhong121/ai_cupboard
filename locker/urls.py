from django.urls import path
from locker import views

urlpatterns = [
    path('', views.Lockerslist.as_view()),                 #unit list
    path('<int:pk>', views.LockersDetail.as_view()),     #unit Detail
    path('cabinet',views.Cabinetlist.as_view()),                 #category list
    path('cabinet/<int:pk>', views.CabinetDetail.as_view()),      #category Detail
]