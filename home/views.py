from django.http import Http404
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework import generics, status
from rest_framework.response import Response

from .models import HomeCard, HomeSlide
from .serializers import HomeCardSerializer, HomeSlideSerializer


class HomeCardList(generics.ListAPIView):
    def get(self, request, format=None):
        queryset = HomeCard.objects.all()
        serializer = HomeCardSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HomeCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeCardDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self, pk):
        try:
            return HomeCard.objects.get(pk=pk)
        except HomeCard.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = HomeCardSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = HomeCardSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomeSlideList(generics.ListAPIView):
    def get(self, request, format=None):
        queryset = HomeSlide.objects.all()
        serializer = HomeSlideSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HomeSlideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeSlideDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self, pk):
        try:
            return HomeSlide.objects.get(pk=pk)
        except HomeSlide.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = HomeSlideSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = HomeSlideSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
