from django.shortcuts import render
from .models import ComputerScienceModel
from .serializer import ComputerScienceSer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ComputerScienceView(APIView):
    def get (self,r):
        pyobj = ComputerScienceModel.objects.all()
        ser = ComputerScienceSer(pyobj,many = True)
        return Response(ser.data)

    def post (self,r):
        serobj = ComputerScienceSer(data = r.data)
        if serobj.is_valid():
            serobj.save()
            return Response (serobj.data,status = status.HTTP_CREATED)
        return Response(serobj.errors,status = status.HTTP_400_BAD_REQUEST)

class ComputerScienceViewUpdateDelete(APIView):
    def put (self,r,pk):
        obj = ComputerScienceModel.objects.get(pk=pk)
        serobj = ComputerScienceSer(obj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self,r,pk):
        obj = ComputerScienceModel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
