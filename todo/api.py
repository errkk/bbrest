from tastypie.resources import ModelResource, Serializer
from tastypie.authorization import Authorization
from .models import Todo

class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'
        allowed_methods = ['get','delete','post','put']
        authorization = Authorization()
        default_format = "application/json"
        serializer = Serializer()

        always_return_data = True


