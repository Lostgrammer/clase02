#simula el get y el post
from rest_framework import routers
from .api import TodoViewSet, TestViewSet,DeleteAllTodo
from django.urls import path

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos') #creando url de mi api "localhost/api/todos"

#test
router.register('api/test', TestViewSet, 'test')

urlpatterns = router.urls

urlpatterns += [path('api/todos/deleteAll',DeleteAllTodo.as_view(), name='deleteAll'),]

#urlpatterns += router.urls



