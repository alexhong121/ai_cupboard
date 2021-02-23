from django.urls import path
from access import views

#######################alex 2020/09/23 app 登录##############################
urlpatterns = [
    path('locker', views.Locker_acclist.as_view()),
    path('locker/<int:pk>', views.Locker_accDetail.as_view()),
    path('ui', views.UI_acclist.as_view()),
    path('ui/<int:pk>',views.UI_accDetail.as_view()),
    path('ui/uid=<int:pk>', views.Per_UIAccDetail.as_view()),  #profiles detail
    # path('test', views.test.as_view())
]
############################################################################
