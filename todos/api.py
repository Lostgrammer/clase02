from .models import Todo
from rest_framework import viewsets, permissions
from .serializer import TodoSerializer, TestTodoSerializer

class TodoViewSet(viewsets.ModelViewSet): #viewsets: indicamos la clase serializada
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    #indicar el serializer que usa esos datos
    serializer_class = TodoSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
<<<<<<< HEAD
    serializer_class = TestTodoSerializer
=======
    serializer_class = TestTodoSerializer
>>>>>>> neorama
