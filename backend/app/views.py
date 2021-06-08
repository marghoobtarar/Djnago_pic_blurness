from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from rest_framework import status
from .models import *
import blur_detector
import cv2
import cv2

import base64
from io import BytesIO
from PIL import Image
import os

class Imagecheck(APIView):
    def post(self, request):
        try:
            is_blur=False 
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = os.getcwd()+uploaded_file_url
            img = cv2.imread(uploaded_file_url , cv2.IMREAD_GRAYSCALE)

            laplacian_variable = cv2.Laplacian(img,cv2.CV_64F).var()
            
            if laplacian_variable < 100:
                is_blur=True
            else:
                is_blur=False
        except Exception as e:
            return Response({'error_message': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            os.remove(uploaded_file_url)
            cv2.destroyAllWindows()
            return Response({'isBlur':is_blur,'sharpnessRate':laplacian_variable},status=status.HTTP_200_OK)
