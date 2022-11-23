# from django.shortcuts import render
# from django.utils import timezone
# import logging
# from django.conf import settings
# from django.core.files.storage import default_storage
# import numpy as np
# import cv2
# import string
# from keras.models import load_model
# from django.core.files.storage import FileSystemStorage
#
# # from pybo.model import Result
# from .models import Result
#
# # Create your views here.
#
# logger = logging.getLogger('mylogger')
#
# def index(request):
#     return render(request, 'language/index.html')
#
# def upload(request):
#     if request.method == 'POST' and request.FILES['files']:
#
#         #todo form에서 전송한 파일을 획득한다.
#         file = request.FILES['files']
#         print('file >> ',file)
#         logger.error('file', file)
#
#         fs = FileSystemStorage(location='media/tmp', base_url='media/tmp')
#         filename = fs.save(file.name, file)
#         print("filename >> ", filename)
#         # class names 준비
#         class_names = list(string.ascii_lowercase)
#         class_names = np.array(class_names)
#
#         print('class_names > ',class_names)
#         model_path = settings.MODEL_DIR +'/sign_model.h5'
#         # model_path = 'C:\\dev\\aivle-sign-language\signlanguage\model\sign_model.h5'
#
#         model = load_model(model_path)
#         print("\n\n\n\ntmp file path >>>>",fs.url(filename))
#
#
#         #todo 흑백으로 읽기
#         # model에서 ImageField로 처리된 항목은 ImageFieldFile 객체로 활용됩니다.
#         # 해당 객체에는 path를 얻어오는 method가 있습니다.
#
#         print("*1"*50)
#         #todo 크기 조정
#
#         #todo input shape 맞추기
#         img = cv2.imread(fs.url(filename), cv2.IMREAD_GRAYSCALE)
#         #todo 스케일링
#         img = cv2.resize(img, (28,28))
#         img = img.reshape(1,28,28,1)
#         img = img/255.
#
#         #todo 예측 : 결국 이 결과를 얻기 위해 모든 것을 했다.
#         # 예측 결과를 수행해보세요.
#         pred = model.predict(img)
#         print("*"*50)
#         pred2 = pred.argmax(axis=1)
#         print("pred >>> ",pred.argmax(axis=1))
#         print("*"*50)
#
#         result = Result()
#         # result.answer =model.predict(axis=)
#         result.answer = request.POST.get('answer','')
#         print("fs.url(filename) >> ",fs.url(filename))
#         result.image = file
#         result.pub_date = timezone.datetime.now()
#         result.save()
#
#
#
#
#         print('result : ', class_names[pred2][0])
#         #todo 예측 결과를 DB에 저장한다.
#         result.result = class_names[pred2][0]
#         result.save()
#
#         context = {
#             'result': result,
#         }
#
#         #todo history 저장을 위해 객체에 담아서 DB에 저장한다.
#         # 이때 파일시스템에 저장도 된다.
#
#
#     # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠.
#     else:
#         test = request.GET['test']
#         logger.error(('Something went wrong!!',test))
#
#     return render(request, 'language/result.html', context)
#
