from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import BooksSerializer
from .models import Books


# 1st Method
class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Books.objects.all()
        serializer = BooksSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# 2nd Method
class BooksView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 3th Method
class BooksCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# 4th Method
class BooksListCreateView(generics.ListCreateAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()