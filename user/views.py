from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PasswordChangeSerializer
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail

from user.serializers import UserSerializers, PasswordChangeSerializer, PasswordResetSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        serializer.save()


class PasswordChangeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password has been successfully changed.'}, status=status.HTTP_200_OK)


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        uid = data['uid']
        token = data['token']
        email = serializer.validated_data['email']

        reset_link = f'http://127.0.0.1:8000/api/accounts/reset/{uid}/{token}/'

        send_mail(
            'Password Reset',
            f'Use the following link to reset your password: {reset_link}',
            'ahmad1519@gmail.com',
            [user.email],
            fail_silently=False,
        )

        return Response({'detail': 'Password reset link has been sent to your email.'}, status=status.HTTP_200_OK)