from django.shortcuts import render
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
from keras.models import load_model
from django.core.files.storage import FileSystemStorage

# from pybo.model import Result
from .models import Result

# Create your views here.

logger = logging.getLogger('mylogger')

def index(request):
    return render(request, 'language/index.html')

def upload(request):
    if request.method == 'POST' and request.FILES:
        print('='*50)
        print('1')
        
        # form 에서 받은 값 : file list, answer[]
        file = request.FILES.getlist('files')
        print('files >> ',file)
        print('file length >> ',len(file))
        print('file[0] >> ',file[0])
       
        # class names 준비 & model 불러오기
        class_names = list(string.ascii_lowercase)
        class_names = np.array(class_names)
        model_path = settings.MODEL_DIR +'/sign_model.h5'
        model = load_model(model_path) 
        
        # 파일 저장
        pred2 = []
        resultList = []
        answers = request.POST.getlist('answer[]')
        
        for i,el in enumerate(file):
            fs = FileSystemStorage(location='media/tmp', base_url='media/tmp')
            filename = fs.save(file[i].name, file[i])
            print('el : ', el)
            print('filename : ',filename)
            
            # Upload Image 전처리
            img = cv2.imread(fs.url(filename), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (28,28))
            img = img.reshape(1,28,28,1)
            img = img/255.
            
            # Predict
            pred = model.predict(img) 
            print("pred >>> ",pred.argmax(axis=1))
            pred2.append(pred.argmax(axis=1))
            
            result = Result()
            result.answer = answers[i]
            result.image = file[i]
            result.pub_date = timezone.datetime.now()
            
            print("result.answer : ",result.answer)
            
            if result.answer != class_names[pred2[i]][0]:
                result.ret = '틀렸습니다!'
            else:  
                result.ret = '맞았습니다!'
            result.result = class_names[pred2[i]][0]
            # print('pred2 : ', class_names[pred2[i]][0] )
            
            result.save()
            resultList.append(result)
            
        # return 할 결과
    
        # result = Result()
        # result.answer = request.POST.getlist('answer[]')
        # result.image = file
        # result.pub_date = timezone.datetime.now()
        
       
        # print('answer >> ', result.answer)
        # print('answer len >> ', len(result.answer))
        
        # result.save()
        print("*"*50)
        
        # if result.answer != class_names[pred2][0]:
        #     result.ret = '틀렸습니다!'
        # else:  
        #     result.ret = '맞았습니다!'
        
        # print('result : ', class_names[pred2][0])
        #todo 예측 결과를 DB에 저장한다.
        # result.result = class_names[pred2][0]
        # result.save()

        context = {
            'resultList': resultList,
        }

        #todo history 저장을 위해 객체에 담아서 DB에 저장한다.
        # 이때 파일시스템에 저장도 된다.
  

    # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠.
    else:
        test = request.GET['test']
        logger.error(('Something went wrong!!',test))

    return render(request, 'language/result.html', context)    

