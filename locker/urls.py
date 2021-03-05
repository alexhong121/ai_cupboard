from django.urls import path
from locker import views

urlpatterns = [
    path('', views.Lockerslist.as_view()),                 #抽屜 list
    path('<int:pk>', views.LockersDetail.as_view()),     #抽屜 Detail
    path('cabinet',views.Cabinetlist.as_view()),                 #櫃 list
    path('cabinet/<int:pk>', views.CabinetDetail.as_view()),      #櫃 Detail
    path('init', views.InitializeLockView.as_view()),      #初始化 抽屜列表
]