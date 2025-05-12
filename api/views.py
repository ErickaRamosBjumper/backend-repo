from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import yaml
import os
def load_api_spec():
    api_spec_path = os.path.join(os.path.dirname(__file__), '..', 'api-contract', 'api-spec.yaml')
    with open(api_spec_path, 'r') as file:
        return yaml.safe_load(file)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar usuarios.
    Implementa el contrato de API definido en el submódulo.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request):
        # Implementación del endpoint GET /users
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        # Implementación del endpoint GET /users/{id}
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)
