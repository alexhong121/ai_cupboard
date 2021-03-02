import logging

from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status


from users.models import Profiles,Departments,Questions,Quest_answers
from users.serializers import ProfilesSerializer,AuthUserSerializer,Quest_answersSerializer,QuestionsSerializer,DepartmentsSerializer,MyTokenRefreshSerializer

from users.core import check_login,verify_account,RegisterAccount,reset_password,check_answer
from utils.base import filter_profiles_object,content,DataFormat,get_model_object
from access.data import ui
from access.serializers import UI_accessSerializers

# Create your views here.
class ProcessDataTools():

    def __init__(self):
        self.data={}
        self.row=''

    @classmethod
    def form_data_save(cls, request,row):
        cls.data=request.data.dict()
        cls.data[row]=cls.data.pop('uid')

        return cls.data
    @classmethod
    def json_save(cls,data,row):
        cls.data=data
        cls.data.setdefault(row,data['uid'])

        return cls.data


class Userslist(APIView):
    """
    List all Users, or create a new Users.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # data = ProcessDataTools.form_data_save(request,'create_uid')
        serializer = ProfilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(
                types='error',  # 相应的状态 'success'
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class UsersDatail(APIView):
    """
    Retrieve, update or delete a Users instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Profiles.objects.get(pk=pk)
        except Profiles.DoesNotExist:
            raise Http404
    
    def put(self, request,pk, format=None):
        profiles = self.get_object(pk)
        serializer = ProfilesSerializer(profiles, data=request.data)
        format=DataFormat()
        if serializer.is_valid():
            serializer.save()
            return Response(format.content(data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(format.error(
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class ProfilesDetail(APIView):

    def get(self, request, pk, format=None):
        profiles=filter_profiles_object(pk)
        serializer = ProfilesSerializer(profiles, many=True)
        format=DataFormat()

        return Response(format.content(
            data=serializer.data
            ),status=status.HTTP_200_OK)

class LoginOutAccountView(APIView):

    def post(self, request, format=None):
        """
        Login Account
        """
        result = check_login(request)

        if result['type'] == 'success':
            return Response(result,status=status.HTTP_200_OK)
        else:
            return Response(result,status=status.HTTP_200_OK)

    def get(self, request, format=None):
        """
        Logout Account
        """
        logout(request)
        dataFormat=DataFormat()
        return Response(dataFormat.success(message="logout of the account"),status=status.HTTP_200_OK)
    
class VerifyAccountView(APIView):
    """
    Verify account
    """
    def post(self, request, format=None):
        result=verify_account(request)
        if result['type'] == 'success':
            return Response(result,status=status.HTTP_200_OK)
        else:
            return Response(result,status=status.HTTP_200_OK)


class RegistrationView(APIView):
    
    def post(self, request, format=None):
        """
        2020/09/29 alex 註冊api
        """
        jsonData = JSONParser().parse(request)

        registerAccount=RegisterAccount(jsonData)
        result=registerAccount.process()

        if result['type'] == 'success':
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(result,status=status.HTTP_201_CREATED)


class RestPasswordView(APIView):

    def put(self, request, pk, format=None):
        """
        reset password
        """
        result=reset_password(pk=pk,model=User,request=request)

        if result['type'] == 'success':
            return Response(result,status=status.HTTP_200_OK)
        else:
            return Response(result,status=status.HTTP_400_BAD_REQUEST)

class QuestionslistView(APIView):
    """
    List all Questions, or create a new Questions.
    """
    def get(self, request, format=None):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        dataFormat=DataFormat()
        return Response(dataFormat.success(data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        dataFormat=DataFormat()
        processData=ProcessDataTools.json_save(data,'create_uid')
        serializer = QuestionsSerializer(data=processData)
        if serializer.is_valid():
            serializer.save()
            return Response(dataFormat.content(data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(dataFormat.error(
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class VerifyAnswerView(APIView):

    def post(self, request, format=None):
        try:
            result = check_answer(request)

            if result['type'] == 'success':
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(e)
            dataFormat=DataFormat()
            return Response(dataFormat.error(message="Profile does not exist!!"),status=status.HTTP_404_NOT_FOUND)        

class Departmentslist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        departments = Departments.objects.all()
        serializer = DepartmentsSerializer(departments, many=True)
        # content={
        #     'type': 'success',  # 相应的状态 'success' | "error"
        #     'data': serializer.data, # 主要的数据 [ ] | { }
        #     'message':None     # 错误信息
        # }
        return Response(content(
            types='success',  # 相应的状态 'success' | "error"
            data=serializer.data
        ),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DepartmentsSerializer(data=request.data['params'])
        if serializer.is_valid():
            serializer.save()
            # content={
            #     'type': 'success',  # 相应的状态 'success' | "error"
            #     'data': serializer.data, # 主要的数据 [ ] | { }
            #     'message':None     # 错误信息
            # }
            return Response(content(
                types='success',  # 相应的状态 'success' | "error"
                data=serializer.data
            ), status=status.HTTP_201_CREATED)
        # content={
        #     'type': 'success',  # 相应的状态 'success' | "error"
        #     'data': None, # 主要的数据 [ ] | { }
        #     'message':serializer.errors     # 错误信息
        # }

        return Response(content(
            types='success',  # 相应的状态 'success' | "error"
            message=serializer.errors
        ), status=status.HTTP_400_BAD_REQUEST)


class DepartmentsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Departments.objects.get(pk=pk)
        except Departments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        departments = self.get_object(pk)
        serializer = DepartmentsSerializer(departments)\

        return Response(content(
            types='success',  # 相应的状态 'success' | "error"
            data=serializer.data
        ),status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        departments = self.get_object(pk)
        serializer = DepartmentsSerializer(departments, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(content(
                types='success',
                data=serializer.data
            ),status=status.HTTP_200_OK)

        return Response(content(
            types='error',  # 相应的状态 'success'
            message=serializer.errors
        ), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        departments = self.get_object(pk)
        departments.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer