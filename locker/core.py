import logging

from django.db import transaction
from django.http import Http404

from locker.models import Cabinet,Lockers
from locker.serializers import CabinetSerializer,LockersSerializer
from utils.base import DataFormat

dataFormat = DataFormat()

class LockerTools():

    def __init__(self):
        self.__serializer=None
        self.__data={
            "location":"",
            "code":"",
            "name":"",
            "lock_time":0,
            "Cabinet_id":"",
            "Pro_cate_id":"",
            "status":False
        }

    @transaction.atomic
    def initial(self):
        cabinet= Cabinet.objects.all().first()
        if cabinet is not None:
            sid = transaction.savepoint()
            try:
                for i in range(int(cabinet.column)):
                    for j in range(int(cabinet.row)):
                        self.__data.update({
                            "location":"{0},{1}".format(i,j),
                            "Cabinet_id":cabinet.id
                        })
                        self.__serializer= LockersSerializer(data=self.__data)
                        if self.__serializer.is_valid():
                            self.__serializer.save()
                        else:
                            raise ValueError(self.__serializer.errors) 
                transaction.savepoint_commit(sid)
                return dataFormat.success(message="initialization is finish!!")
            except ValueError as e:
                logging.error(e)
                transaction.savepoint_rollback(sid)

                return dataFormat.error(message=self.__serializer)    
            except Exception as e:
                logging.error(e)
                transaction.savepoint_rollback(sid)

                return dataFormat.error(message=self.__serializer)
        
                