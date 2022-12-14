from .models import Todo
from rest_framework import viewsets, permissions
from .serializer import TodoSerializer, TestTodoSerializer
#nuevos
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class TodoViewSet(viewsets.ModelViewSet): #viewsets: indicamos la clase serializada
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
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
