
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

from utils.base import get_profiles_object,content,Format
from access.data import ui
from access.serializers import UI_accessSerializers

# content={
#    'type': None,  # 相应的状态 'success' | "error"
#    'data': None, # 主要的数据 [ ] | { }
#    'message':None     # 错误信息
# }

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
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(
                types='error',  # 相应的状态 'success'
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class ProfilesDetail(APIView):

    def get(self, request, pk, format=None):
        profiles=get_profiles_object(pk)
        serializer = ProfilesSerializer(profiles, many=True)

        # content={
        #     'type': 'success',  # 相应的状态 'success' | "error"
        #     'data': serializer.data, # 主要的数据 [ ] | { }
        #     'message':None     # 错误信息
        # }
        


        return Response(content(
            types='success',
            data=serializer.data
            ),status=status.HTTP_200_OK)

class Login_validation(APIView):
    
    def post(self, request, format=None):
        result = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        format=Format()
        if result is not None and result.is_active:
            login(request, result)
            user=User.objects.filter(username=result).first()
            refresh = RefreshToken.for_user(user)

            return Response(format.content(
                data={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "uid":user.id,
                }
            ),status=status.HTTP_200_OK)
        else:

            return Response(format.error(
               message='account is fault' 
            ),status=status.HTTP_200_OK)
    
class Logout(APIView):

    def get(self, request, format=None):
        logout(request)
        format=Format()
        return Response(fromat.content(message="logout of the account "),status=status.HTTP_200_OK)


class Accounts_validation(APIView):

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        user=User.objects.filter(username=data["params"]['username']).first()
        format=Format()
        if user is not None:

            return Response(format.content(
                data={
                    "uid":user.id    #id of currnt account
                }
            ),status=status.HTTP_200_OK)
        else:
            # content={
            #     "message":"account is not existed!!",
            # }
            return Response(format.error(
                message='account is not existed!!'
                ),status=status.HTTP_404_NOT_FOUND)
        return Response(status=HTTP_400_BAD_REQUEST)


class RegistrationApp(APIView):
    
    def __init__(self):
        self._errorsFlag=False
        self._serializer={}
        self._data={}

    def initial_access(self):
        
        for record in ui:
            record.update({'Profiles_id':self._data['Profiles_id']})
            ui_access=UI_accessSerializers(data=record)
            if ui_access.is_valid():
                ui_access.save()
                self._errorsFlag=False
            else:
                self._errorsFlag=True
                self._serializer=ui_access

    @transaction.atomic
    def registration_flow(self):
        
        sid = transaction.savepoint()

        try:
            # create_authUser
            self._serializer=AuthUserSerializer(data=self._data["authUserData"])
            if self._serializer.is_valid():
                self._serializer.save()
            else:
                raise ValueError("有問題啦")
            # create_profiles
            self._data["profilesData"].update({"AuthUser_id":authUserSerializer.data['id']})    
            self._serializer = ProfilesSerializer(data=self._data["profilesData"])

            if self._serializer.is_valid():
                self._serializer.save()
            else:
                raise ValueError("pro have problems")
            # create_answer
            self._data.update({'Profiles_id':profilesSerializer.data['id']})

            for result in self._data["answerData"]:

                answerdict={
                    "answer":result['answer'],
                    "Profiles_id":self._data['Profiles_id'],
                    "Questions_id":result['Questions_id']
                }

                self._serializer=Quest_answersSerializer(data=answerdict)
                if self._serializer.is_valid():
                    self._serializer.save()
                else:
                    raise ValueError("pro have problems")

            transaction.savepoint_commit(sid)
        except ValueError as e:
            self._errorsFlag=True
            transaction.savepoint_rollback(sid)
        except:
            self._errorsFlag=True
            transaction.savepoint_rollback(sid)

    def post(self, request, format=None):
        """
        2020/09/29 alex 註冊api
        """
        jsonData = JSONParser().parse(request)
        
        self._data={
            "Profiles_id":None,
            "profilesData":{
                "AuthUser_id":None,
                "name":jsonData['params']['Profiles_id']["name"]
            },
            "answerData":jsonData['params']['Answer_ids'],
            "authUserData": {
                                'username':jsonData['params']['AuthUser_id']['username'],
                                'password':make_password(jsonData['params']['AuthUser_id']['password'])
                            }
        }
    
        self.registration_flow()

        format=Format()

        if self._errorsFlag:
            return Response(format.error(
                message=self._serializer.errors
            ),status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(format.content(
                data={
                    "uid":self._data["profilesData"]['AuthUser_id']
                },
                message="the data is created successfully!!"),status=status.HTTP_201_CREATED)


class AccountsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        User = self.get_object(pk)
        data={
            "username":User.username,
            "password":make_password(request.data.get('password'))
        }
        serializer = AuthUserSerializer(User, data=data)
        if serializer.is_valid():
            serializer.save()
            # content={
            #     'type': 'success',  # 相应的状态 'success' | "error"
            #     'data': None, # 主要的数据 [ ] | { }
            #     'message':"The password id writed"     # 错误信息
            # }
            return Response(content(
                types='success',  # 相应的状态 'success' | "error"
                message='The password id writed'
            ),status=status.HTTP_200_OK)
        # content={
        #     'type': 'error',  # 相应的状态 'success' | "error"
        #     'data': None, # 主要的数据 [ ] | { }
        #     'message':"serializer.errors"     # 错误信息
        # }

        return Response(content(
            types='error',  # 相应的状态 'success'
            message=serializer.errors
        ), status=status.HTTP_400_BAD_REQUEST)

class Questionslist(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)

        processData=ProcessDataTools.json_save(data,'create_uid')
        serializer = QuestionsSerializer(data=processData)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(
                types='error',  # 相应的状态 'success'
                message=serializer.error
            ),status=status.HTTP_400_BAD_REQUEST)

class Quest_answer_validation(APIView):


    def post(self, request, format=None):
        data = JSONParser().parse(request)
        answers=data['params']['Answer_ids']
        profiles=get_profiles_object(data['uid']).first()

        if profiles is not None:
            for i in range(len(answers)):
                quest_answers=Quest_answers.objects.filter(
                    Profiles_id=profiles.id,
                    Questions_id=answers[i]['Questions_id'],
                    answer=answers[i]['answer']).first()

                if quest_answers is None:

                    # content_dict.append({
                    #     'type': 'error',  # 相应的状态 'success' | "error"
                    #     'data': {'Question_id':answers[i]['Questions_id']}, # 主要的数据 [ ] | { }
                    #     'message':"the answer is wrong!"     # 错误信息
                    # })


                    return Response(content(
                        types='error',  # 相应的状态 'success'
                        message="the answer is wrong!"
                    ),status=status.HTTP_400_BAD_REQUEST)
                else:
                    # content_dict.append({
                    #     'type': 'success',  # 相应的状态 'success' | "error"
                    #     'data': {'Question_id':answers[i]['Questions_id']}, # 主要的数据 [ ] | { }
                    #     'message':"The answer is all right"     # 错误信息
                    # })
                    return Response(content(
                        types='success',  # 相应的状态 'success' | "error"
                        message="The answer is all right"
                    ),status=status.HTTP_200_OK)   
                 
        else:
            # content={
            #     'type': 'error',  # 相应的状态 'success' | "error"
            #     'data': None, # 主要的数据 [ ] | { }
            #     'message':"Profile does not exist"     # 错误信息
            # }

            return Response(content(
                types='error',  # 相应的状态 'success'
                message='Profile does not exist'
            ),status=status.HTTP_400_BAD_REQUEST)


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
        serializer = DepartmentsSerializer(departments)

        # content={
        #     'type': 'success',  # 相应的状态 'success' | "error"
        #     'data': serializer.data, # 主要的数据 [ ] | { }
        #     'message':None     # 错误信息
        # }   

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