import logging

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db.utils import IntegrityError

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status

from users.models import Profiles,Departments,Questions,Quest_answers
from users.serializers import ProfilesSerializer,QuestionsSerializer,DepartmentsSerializer,MyTokenRefreshSerializer

from users.core import check_login,verify_account,RegisterAccount,reset_password,check_answer
from utils.base import filter_profiles_object,DataFormat,get_model_object



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


class UserslistView(APIView):
    """
    List all Users, or create a new Users.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        dataFormat=DataFormat()
        return Response(dataFormat.success(data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProfilesSerializer(data=request.data)
        dataFormat=DataFormat()
        if serializer.is_valid():
            serializer.save()
            return Response(dataFormat.success(data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(dataFormat.error(
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class ProfilesAuthUserView(APIView):
    """
    Retrieve, update or delete a Users instance.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        profiles=filter_profiles_object(pk)
        serializer = ProfilesSerializer(profiles, many=True)
        dataFormat=DataFormat()

        return Response(dataFormat.success(
            data=serializer.data
            ),status=status.HTTP_200_OK)

class ProfilesDetailView(APIView):
    """
    Retrieve, update or delete a Users instance.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        profiles=filter_profiles_object(pk)
        serializer = ProfilesSerializer(profiles, many=True)
        dataFormat=DataFormat()

        return Response(dataFormat.success(
            data=serializer.data
            ),status=status.HTTP_200_OK)
    
    def put(self, request,pk, format=None):
        profiles=filter_profiles_object(pk).first()
        serializer = ProfilesSerializer(profiles, data=request.data)
        dataFormat=DataFormat()

        if serializer.is_valid():
            serializer.save()
            return Response(dataFormat.success(data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(dataFormat.error(
                message=serializer.errors
            ),status=status.HTTP_400_BAD_REQUEST)

class upload_to_image(APIView):
    def post(self, request, pk , format=None):
        profiles=filter_profiles_object(pk).first()
        serializer = ProfilesSerializer(profiles, data=request.data)
        dataFormat=DataFormat()

        if serializer.is_valid():
            serializer.save()
            return Response(dataFormat.success(data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(dataFormat.error(
                message=serializer.errors
            ),status=status.HTTP_400_BAD_REQUEST)


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
            return Response(result,status=status.HTTP_201_CREATED)
        else:
            return Response(result,status=status.HTTP_400_BAD_REQUEST)


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
            return Response(dataFormat.success(data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(dataFormat.error(
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class VerifyAnswerView(APIView):

    def post(self, request, format=None):
        print(request)

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


class DepartmentslistView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    dataFormat=DataFormat()

    def get(self, request, format=None):
        departments = Departments.objects.all()
        serializer = DepartmentsSerializer(departments, many=True)
        dataFormat=DataFormat()
        return Response(dataFormat.success(
            data=serializer.data
        ),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DepartmentsSerializer(data=request.data['params'])
        dataFormat=DataFormat()
        if serializer.is_valid():
            serializer.save()
            return Response(dataFormat.success(
                data=serializer.data
            ), status=status.HTTP_201_CREATED)
        else:
            return Response(dataFormat.error(
                message=serializer.errors
            ), status=status.HTTP_400_BAD_REQUEST)


class DepartmentsDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk, format=None):
        departments = get_model_object(pk=pk,model=Departments)
        serializer = DepartmentsSerializer(departments)
        dataFormat=DataFormat()
        return Response(dataFormat.success(
            data=serializer.data
        ),status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        departments = get_model_object(pk=pk,model=Departments)
        serializer = DepartmentsSerializer(departments, data=request.data)
        dataFormat=DataFormat()
        if serializer.is_valid():
            serializer.save()

            return Response(dataFormat.success(
                data=serializer.data
            ),status=status.HTTP_200_OK)
        else:
            return Response(dataFormat.error(
                message=serializer.errors
            ), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        departments = get_model_object(pk=pk,model=Departments)
        departments.delete()
        dataFormat=DataFormat()
        return Response(dataFormat.success(message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer