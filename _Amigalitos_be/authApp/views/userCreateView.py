from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializaers.userSerializer import UserSerializer

class UserCreateView(view.APIView):
    def post(self, request, *args, **kwargs):
        # En esta porte la petición es leída
        # En rquest se obtiene la petición (request - request header - body)
        # El request.data se recibe como json
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)