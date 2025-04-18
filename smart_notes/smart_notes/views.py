from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class root(APIView):
    def get(self,request):
        return Response({'msg':'hello,world!'},status=status.HTTP_200_OK)