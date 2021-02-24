from users.models import Profiles
from django.http import Http404

# CONTENT_STRUCTURE={
#    'type': None,  # 相应的状态 'success' | "error"
#    'data': None, # 主要的数据 [ ] | { }
#    'message':None     # 错误信息
# }

def filter_profiles_object(pk):
    try:
        return Profiles.objects.filter(AuthUser_id=pk)
    except Profiles.DoesNotExist:
        raise Http404("Profiles does not exist")

def content(types=None,data=None,message=None):
    CONTENT_STRUCTURE={
        'type': types,  # 相应的状态 'success' | "error"
        'data': data, # 主要的数据 [ ] | { }
        'message':message     # 错误信息
    }

    return CONTENT_STRUCTURE

def get_model_object(pk,model):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404("%s does not exist" % model)

class DataFormat(object):
    def __init__(self):
        self._CONTENT_STRUCTURE={
            'type': None,  # 相应的状态 'success' | "error"
            'data': None, # 主要的数据 [ ] | { }
            'message':None     # 错误信息
        }

    def content(self,data=None,message=None):

        self._CONTENT_STRUCTURE.update({
            'type':'success',
            'data': data, # 主要的数据 [ ] | { }
            'message':message     # 错误信息
        })
        return self._CONTENT_STRUCTURE
    
    def error(self,data=None,message=None):
        self._CONTENT_STRUCTURE.update({
            'type':'error',
            'data': data, # 主要的数据 [ ] | { }
            'message':message     # 错误信息
        })
        return self._CONTENT_STRUCTURE