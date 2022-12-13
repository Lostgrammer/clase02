#simula el get y el post
from rest_framework import routers
from .api import TodoViewSet, TestViewSet

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos') #creando url de mi api "localhost/api/todos"

router.register('api/test', TestViewSet, 'test')

urlpatterns = router.urls #todas la rutas

