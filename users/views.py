from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from django.conf import settings
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10), #Token will be valid for 10 days
            'iat': datetime.datetime.utcnow() # Date Time when the token is created
        }

        token = jwt.encode(payload, settings.TOKEN_SECRET, algorithm='HS256')

        return Response({'token': token})


class ConnUserView(APIView):

    def get(self, request):
        if "Authorization" not in request.headers:
            raise AuthenticationFailed('Unauthorized')

        token_prefix = request.headers["Authorization"][0:6]
        token = request.headers["Authorization"][7:]

        if token_prefix != "Bearer":
            raise AuthenticationFailed('Unauthorized')

        if token is None:
            raise AuthenticationFailed('Unauthorized')

        try:
            payload = jwt.decode(token, settings.TOKEN_SECRET, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
