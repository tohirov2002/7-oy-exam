from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from .models import Commander
from .serializers import CommanderListSerializer
from .filters import CommanderFilter


# class IsCommanderInfo(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return view.get_object().commander_user == request.user


class CommanderListView(viewsets.ModelViewSet):
    queryset = Commander.objects.all()
    serializer_class = CommanderListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommanderFilter
