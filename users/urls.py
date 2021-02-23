from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#######################alex 2020/09/23 app 登录##############################
urlpatterns = [
    path('', views.Userslist.as_view()),    #users list
    path('<int:pk>',views.UsersDatail.as_view()),
    path('login', views.Login_validation.as_view()),     #login
    path('logout',views.Logout.as_view()),
    path('registration', views.RegistrationApp.as_view()),  #註冊
    path('psforget',views.Accounts_validation.as_view()),   #forget password V
    path('questions',views.Questionslist.as_view()), # questions    
    path('authUser/uid=<int:pk>',views.AccountsDetail.as_view()),   #修改密碼 
    path('questions/validation',views.Quest_answer_validation.as_view()), #validation problems
    path('departments', views.Departmentslist.as_view()),# 部門list
    path('departments/<int:pk>',views.DepartmentsDetail.as_view()),
    path('uid=<int:pk>', views.ProfilesDetail.as_view()),  #profiles detail
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh/', views.MyTokenRefreshView.as_view()),

    
]
############################################################################

