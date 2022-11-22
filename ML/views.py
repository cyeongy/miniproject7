<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render,redirect
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
from keras.models import load_model
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *

logger = logging.getLogger('mylogger')

## 모델 등록 받는 화면 
def index(request):
    return render(request, 'ML/index.html')

# def ml_model_create(request):
#     if request.method=='POST':
#         form=MakeMLModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # post=Post.objects.create(**form.cleaned_data)
#             ml_model=form.save()
#             return redirect(ml_model)
#     else:
#         form=MakeMLModelForm()
#         return render(request, 'ML/ml_model_form.html',{'form':form})
    
    
# def list(request):
#     model_list = ML_Model.objects.all()      
    
#     return render(request, 'ML/list.html', {'model_all':model_list})

## 모델 업로드하면 모델을 FILEField로 받아 저장하고, DB에는 모델명
def upload(request):

    if request.method == 'POST' and request.FILES['files']:

        #todo form에서 전송한 파일을 획득한다.
        file = request.FILES['files']
        # print('file >> ',file)
        # logger.error('file', file)
        
        fs = FileSystemStorage(location='media/loaded_model', base_url='media/loaded_model')
        filename = fs.save(file.name, file)
       
        # print("filename >> ", filename)


    # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠.
    else:
        pass

    return render(request, 'ML/list.html')

>>>>>>> eb2fa32 (Rebase commit)
