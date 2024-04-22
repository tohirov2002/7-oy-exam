from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PasswordChangeSerializer
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from user.serializers import UserSerializers, PasswordChangeSerializer, PasswordResetSerializer
from rest_framework.views import APIView
from rest_framework import status


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

        # Foydalanuvchi obyektini olish
        user = get_user_model().objects.get(email=email)

        reset_link = f'http://127.0.0.1:8000/api/accounts/reset/{uid}/{token}/'

        send_mail(
            'Password Reset',
            f'Use the following link to reset your password: {reset_link}',
            'ahmad1519@gmail.com',
            [user.email],  # Foydalanuvchining email manzili
            fail_silently=False,
        )


class EmailConfirmationView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            current_site = get_current_site(request)
            mail_subject = 'Email Confirmation'
            message = render_to_string('email_confirmation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
            send_mail(mail_subject, message, 'from@example.com', [email])
            return Response({'message': 'Confirmation email sent.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
