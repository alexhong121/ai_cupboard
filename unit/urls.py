from django.urls import path
from unit import views

#######################alex 2020/09/23 app 登录##############################
urlpatterns = [
    path('', views.Unitlist.as_view()),                 #unit list
    path('<int:pk>', views.UnitDetail.as_view()),     #unit Detail
    path('category',views.Categorylist.as_view()),                 #category list
    path('category/<int:pk>', views.CategoryDetail.as_view()),      #category Detail
]
############################################################################