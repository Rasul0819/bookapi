from django.shortcuts import render,get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView)

from bookapp.models import *
from .serializers import *
from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework import status


class BookCreateApiView(APIView):
    def post(self,request):
        data = request.data
        serializer = BooksSerializerClass(data=data)
        try:
                
            if serializer.is_valid():
                serializer.save()
                data = {
                        'status':'You added a  book))))',
                        'book':data
                    }
                return Response(data)
        except Exception:
            return Response(
                {
                    'status':False,
                    'message':'qatelik bar'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


# class BooksApiView(ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass


class BooksApiView(APIView):
    def get(self,request):
        books = Books.objects.all()
        serializer_data = BooksSerializerClass(books,many=True).data
        context = {
            'status':'Kitaplar qaytarildi',
            'books':serializer_data
        }
        return Response(context)


# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass
class BookDetailView(APIView):
    def get(self,request,pk):

        try:

            book = Books.objects.get(id=pk)#get_object_or_404
            serializer_data = BooksSerializerClass(book).data

            context = {
                'status':'Detail ashildi',
                'book':serializer_data
            }
            return Response(context)
        except Exception:
            return Response(
                {'status':False,
                 'messgae':'qatelik ketti'},
                 status=status.HTTP_404_NOT_FOUND)
        

# class BookCreateApiView(CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass
class BookUpdateView(APIView):
    def put(self,request,pk):
        books = Books.objects.all()
        book = get_object_or_404(books,id=pk)
        data = request.data
        serializer_data = BooksSerializerClass(instance=book,data=data,partial=True)
        if serializer_data.is_valid(raise_exception=True):
            book_saved = serializer_data.save()
            context = {
                'status':True,
                'message':f'Kitap ozgerdi:{book_saved}'
            }
        return Response(context)


class BookDeleteView(APIView):
    def delete(self,request,pk):
        books = Books.objects.all()
        book = get_object_or_404(books,id=pk)
        book.delete()
        data = {
            'status':True,
            'message':'Oshirildi'
        }
        return Response(data,status=status.HTTP_200_OK)