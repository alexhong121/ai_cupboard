from django.urls import path
from inv import views


#######################alex 2020/09/23 app 登录##############################
urlpatterns = [
    path('', views.Productlist.as_view()),                 #unit list
    path('<int:pk>', views.ProductDetail.as_view()),     #unit Detail
    path('stock',views.Stocklist.as_view()),                 #category list
    path('stock/<int:pk>', views.StockDetail.as_view()),      #category Detail
    path('stock/out', views.Out_of_the_warehouse.as_view()),      #out of the warehouse
    path('stock/enter', views.Enter_of_the_warehouse.as_view()),      #enter of the warehouse
    path('stock/product/<int:pk>', views.Current_quantity.as_view()), # current_quantity product
]

############################################################################




