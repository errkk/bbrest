from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import TodoResource


v1_api = Api( api_name='v1' )
v1_api.register( TodoResource() )

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls) )
)