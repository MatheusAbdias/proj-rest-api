from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Returna uma lista de funções da APIView"""
        an_apiview = [
            'Usando Http metodos (get,post,put,delete,patch)',
            'É similar a uma tradiciona view do django',
            'te da o controle da logica da aplicação',
            'e mapea manualmente as urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self,request):
        """cria uma messagem de vem vindo com o nome"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk = None):
        """Atualizando um objeto"""
        return Response({'metodo':'put'})
    
    def patch(self,request, pk = None):
        """Atualizando um campo de um objeto"""
        return Response({'metodo':'Patch'})
    
    def delete(self, request, pk = None):
        """Deletando um objeto"""        
        return Response({'methodo':'Delete'})