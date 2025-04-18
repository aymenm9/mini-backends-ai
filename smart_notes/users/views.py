from rest_framework.views import APIView
from rest_framework.generics import mixins
from .serializer import UserSerializer,CreateUserSerializerOutPut
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class userView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: CreateUserSerializerOutPut}
    )

    def post(self, request):
        user_Serialized = UserSerializer(data = request.data)
        if user_Serialized.is_valid():
            user = user_Serialized.save()
            refresh = RefreshToken.for_user(user)
            output = CreateUserSerializerOutPut({
                'user':user_Serialized.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            return Response(output.data, status=status.HTTP_201_CREATED)



