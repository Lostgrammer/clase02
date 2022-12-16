#simula el get y el post
from rest_framework import routers
from .api import TodoViewSet, TestViewSet,DeleteAllTodo,AllList,TodoMixinsViewSet
from django.urls import path
#para el token
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos') #creando url de mi api "localhost/api/todos"


#test
#router.register('api/test', TestViewSet, 'test')

#mixins
#router.register('api/mixin',TodoMixinsViewSet,'mixin')

urlpatterns = router.urls
urlpatterns += [
path('api/todos/mixins',TodoMixinsViewSet.as_view(), name='mixins'),
]
"""
urlpatterns = [
    path('api/todos/deleteAll',DeleteAllTodo.as_view(), name='deleteAll'),
    path('api/todos/all',AllList.as_view(), name='all'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
"""
#urlpatterns += router.urls



