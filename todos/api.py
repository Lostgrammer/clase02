from .models import Todo
from rest_framework import viewsets, permissions, generics
from .serializer import TodoSerializer, TestTodoSerializer
#nuevos
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#token
from rest_framework.permissions import IsAuthenticated
#mixins
from rest_framework.settings import api_settings

class TodoViewSet(viewsets.ModelViewSet): #viewsets: indicamos la clase serializada
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    #indicar el serializer que usa esos datos
    serializer_class = TodoSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer

class DeleteAllTodo(APIView):
    def delete(self, request):
        # Elimina todos los registros
        Todo.objects.all().delete()
        # Retorna un status code de 204 indicando que no existe contenido dentro de nuestra base de datos
        return Response(status=status.HTTP_204_NO_CONTENT)

#nueva clase
class AllList(APIView):
    def get(self, request, format=None):
        registros = Todo.objects.all()
        serializer = TodoSerializer(registros, many=True)
        return Response(serializer.data)

#mixins
class CreateTodoMixin:
    #instancias
    def crear_modelo_Todo(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self,serializer):
        serializer.save()
    def get_success_headers(self,data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except(TypeError, KeyError):
            return {}

#clase
class ListModelMixin:
    def listar_todo(self,request,*args,**kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get.serializer(queryset, many=True)
        return Response(serializer.data)

#mixin creado
class TodoMixinsViewSet(ListModelMixin,CreateTodoMixin,generics.GenericAPIView):
    #diciendole cual es el modelo
    queryset = Todo.objects.all
    serializer_class = TodoSerializer
    def get(self, request, *args, **kwargs):
        return self.listar_todo(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.crear_modelo_Todo(request, *args, **kwargs)