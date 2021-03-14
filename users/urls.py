from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#######################alex 2020/09/23 app 登录##############################
urlpatterns = [
    path('', views.UserslistView.as_view()),    #users list
    # path('<int:pk>',views.ProfilesDetailView.as_view()),
    path('login', views.LoginOutAccountView.as_view()),     #login
    path('logout',views.LoginOutAccountView.as_view()),
    path('registration', views.RegistrationView.as_view()),  #註冊
    path('psforget',views.VerifyAccountView.as_view()),   #forget password V
    path('questions',views.QuestionslistView.as_view()), # questions
    path('authUser',views.AuthUserlistView.as_view()),   # list of account   
    path('authUser/uid=<int:pk>',views.RestPasswordView.as_view()),   #修改密碼 
    path('questions/validation',views.VerifyAnswerView.as_view()), #validation problems
    path('departments', views.DepartmentslistView.as_view()),# 部門list
    path('departments/<int:pk>',views.DepartmentsDetailView.as_view()),
    path('uid=<int:pk>', views.ProfilesDetailView.as_view()),  #profiles detail
    path('image/uid=<int:pk>', views.upload_to_image.as_view()),  #upload to image
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh/', views.MyTokenRefreshView.as_view()),

    
]
############################################################################

