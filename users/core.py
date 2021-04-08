import logging

from django.db import transaction
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.tokens import RefreshToken

from access.data import UI
from access.serializers import UI_accessSerializers
from users.serializers import ProfilesSerializer,AuthUserSerializer,Quest_answersSerializer,QuestionsSerializer,DepartmentsSerializer,MyTokenRefreshSerializer
from users.models import Profiles,Departments,Questions,Quest_answers
from utils.base import DataFormat,get_model_object,filter_profiles_object

dataFormat=DataFormat()

class BaseCore():
    """
        common function
    """
    def filter_answer_object(self,Profiles_id,Questions_id):
        try:
            return Quest_answers.objects.filter(Profiles_id=Profiles_id,Questions_id=Questions_id).first()
        except Quest_answers.DoesNotExist:
            raise Http404("Quest_answers does not exist")

    def filter_profiles_object(self,pk):
        try:
            return Profiles.objects.filter(AuthUser_id=pk).first()
        except Profiles.DoesNotExist:
            raise Http404("Profiles does not exist")

    def get_model_object(self,pk,model):

        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404("%s does not exist" % model)



class AuthUserCore(BaseCore):
    """
     帳號相關功能
    """
    def reset_password(self,pk,request):
        """
            重設密碼
        """

        authUser=self.get_model_object(pk=pk,model=User)

        data={
            "username":user.username,
            "password":make_password(request.data.get('password'))
        }

        serializer = AuthUserSerializer(authUser, data=data)

        if serializer.is_valid():
            serializer.save()

            return dataFormat.success(
                message='The password is writed'
            )
        else:

            return dataFormat.error(
                message=serializer.errors
            )

    def questions_answer(self,pk,request):
        """
          回答問題
        """
        profiles=self.filter_profiles_object(pk)
        answer=self.filter_answer_object(Profiles_id=profiles.id,Questions_id=request.data.get('Questions_id'))
        data={
            "Questions_id":request.data.get('Questions_id'),
            "answer":request.data.get('answer'),
            "Profiles_id":profiles.id
        }
        serializer=Quest_answersSerializer(answer,data=data)

        if serializer.is_valid():
            serializer.save()
            return dataFormat.success(
                message='The Quest_answers is writed'
            )
        else:

            return dataFormat.error(
                message=serializer.errors
            )
    def check_login(request):
        """
            檢查登入帳號 並登入
        """
        result = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if result is not None and result.is_active:
            login(request, result)
            user=User.objects.filter(username=result).first()
            refresh = RefreshToken.for_user(user)

            return dataFormat.success(
                data={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "uid":user.id,
                }
            )
        else:

            return dataFormat.error(
                message='account is fault' 
            )

    def check_answer(request):
        profiles=filter_profiles_object(request.data.get('uid')).first()

        if profiles is not None:
            quest_answers=Quest_answers.objects.filter(
                Profiles_id=profiles.id,
                Questions_id=request.data.get('Questions_id'),
                answer=request.data.get('answer')).first()
            print(quest_answers)

            if quest_answers is None: 
                return dataFormat.error(message="the answer is wrong!")
            else:
                return dataFormat.success(message="The answer is correct!")      
        else:
            raise Http404('Profile does not exist')

    def verify_account(request):
        user=User.objects.filter(username=request.data.get('username')).first()
        if user is not None:
            return dataFormat.success(
                data={
                    "uid":user.id    #id of currnt account
                }
            )
        else:
            return dataFormat.error(
                    message='account is not existed!!'
                )


class ResetAuthUser():
    """
        修改密碼API
    """
    def filter_answer_object(self,Profiles_id,Questions_id):
        try:
            return Quest_answers.objects.filter(Profiles_id=Profiles_id,Questions_id=Questions_id).first()
        except Quest_answers.DoesNotExist:
            raise Http404("Quest_answers does not exist")

    def filter_profiles_object(self,pk):
        try:
            return Profiles.objects.filter(AuthUser_id=pk).first()
        except Profiles.DoesNotExist:
            raise Http404("Profiles does not exist")

    def get_model_object(self,pk,model):

        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404("%s does not exist" % model)
            

    def password(self,pk,model,request):
        """
        input: pk,model,request
        output: 
        """

        user=self.get_model_object(pk=pk,model=model)

        data={
            "username":user.username,
            "password":make_password(request.data.get('password'))
        }

        serializer = AuthUserSerializer(user, data=data)

        if serializer.is_valid():
            serializer.save()

            return dataFormat.success(
                message='The password is writed'
            )
        else:

            return dataFormat.error(
                message=serializer.errors
            )

    def questions_answer(self,pk,model,request):
        profiles=self.filter_profiles_object(pk)
        answer=self.filter_answer_object(Profiles_id=profiles.id,Questions_id=request.data.get('Questions_id'))
        data={
            "Questions_id":request.data.get('Questions_id'),
            "answer":request.data.get('answer'),
            "Profiles_id":profiles.id
        }
        serializer=Quest_answersSerializer(answer,data=data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return dataFormat.success(
                message='The Quest_answers is writed'
            )
        else:

            return dataFormat.error(
                message=serializer.errors
            )

def check_login(request):
    """
    input:  request
    output:     data={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "uid":user.id,
                }
    """
    result = authenticate(username=request.data.get('username'), password=request.data.get('password'))
    if result is not None and result.is_active:
        login(request, result)
        user=User.objects.filter(username=result).first()
        refresh = RefreshToken.for_user(user)

        return dataFormat.success(
            data={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                "uid":user.id,
            }
        )
    else:

        return dataFormat.error(
            message='account is fault' 
        )

def check_answer(request):
    profiles=filter_profiles_object(request.data.get('uid')).first()

    if profiles is not None:
        quest_answers=Quest_answers.objects.filter(
            Profiles_id=profiles.id,
            Questions_id=request.data.get('Questions_id'),
            answer=request.data.get('answer')).first()
        print(quest_answers)

        if quest_answers is None: 
            return dataFormat.error(message="the answer is wrong!")
        else:
            return dataFormat.success(message="The answer is correct!")      
    else:
        raise Http404('Profile does not exist')


def verify_account(request):
    user=User.objects.filter(username=request.data.get('username')).first()
    if user is not None:
        return dataFormat.success(
            data={
                "uid":user.id    #id of currnt account
            }
        )
    else:
        return dataFormat.error(
                message='account is not existed!!'
            )




class RegisterAccount():
    """
    input: jsonData
    output:
    """
    def __init__(self,jsonData):
        self.__serializer=None
        self.__data={
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
    
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)



    def __initial_UIaccess(self):
        "晚一點再寫"

        for record in UI:
            record.update({'Profiles_id':self.__data['Profiles_id']})
            self.__serializer=UI_accessSerializers(data=record)
            if self.__serializer.is_valid():
                self.__serializer.save()
            else:
                raise ValueError(self.__serializer.errors)

    def __add_authUser(self):
        if self.__data["authUserData"]['username']=='admin' or self.__data["authUserData"]['username']=='work':
            self.__data["authUserData"].setdefault('is_staff', True)
            self.__data["authUserData"].setdefault('is_superuser', True)
        self.__serializer=AuthUserSerializer(data=self.__data["authUserData"])
        if self.__serializer.is_valid():
            self.__serializer.save()
            self.__data["profilesData"].update({"AuthUser_id":self.__serializer.data['id']})  
        else:
            raise ValueError(self.__serializer.errors)
    
    def __add_profiles(self):
        self.__serializer = ProfilesSerializer(data=self.__data["profilesData"])        
        if self.__serializer.is_valid():
            self.__serializer.save()
            self.__data.update({'Profiles_id':self.__serializer.data['id']})
        else:
            raise ValueError(self.__serializer.errors)

    def __add_answer(self):
        for result in self.__data["answerData"]:

            answerdict={
                "answer":result['answer'],
                "Profiles_id":self.__data['Profiles_id'],
                "Questions_id":result['Questions_id']
            }

            self.__serializer=Quest_answersSerializer(data=answerdict)

            if self.__serializer.is_valid():
                self.__serializer.save()
            else:
                raise ValueError(self.__serializer.errors)


    @transaction.atomic
    def process(self):
        """
        registration
        """
        sid = transaction.savepoint()
        
        try:
            # create_authUser
            self.__add_authUser()
            # create_profiles
            self.__add_profiles()
            # create_answer
            self.__add_answer()
            # initial_UIaccess
            self.__initial_UIaccess()


            transaction.savepoint_commit(sid)
            return dataFormat.success(data={
                    "uid":self.__data["profilesData"]['AuthUser_id']
                },)
        except ValueError as e:
            logging.error(e)
            transaction.savepoint_rollback(sid)

            return dataFormat.error(message=self.__serializer.errors)
        except Exception as e:
            logging.error(e)
            transaction.savepoint_rollback(sid)

            return dataFormat.error(message=self.__serializer.errors)
        