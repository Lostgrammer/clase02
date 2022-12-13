#simula el get y el post
from rest_framework import routers
from .api import TodoViewSet

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos') #creando url de mi api "localhost/api/todos"

urlpatterns = router.urls #todas la rutas
