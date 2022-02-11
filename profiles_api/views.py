from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Returna uma lista de funções da APIView"""
        an_apiview = [
            'Usando Http metodos (get,post,put,delete,patch)',
            'É similar a uma tradiciona view do django',
            'te da o controle da logica da aplicação',
            'e mapea manualmente as urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})