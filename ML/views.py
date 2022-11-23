from django.shortcuts import render, redirect
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *

logger = logging.getLogger('mylogger')


def list(request):
    model_list = ML_Model.objects.all()
    return render(request, 'ML/list.html', {'model_all': model_list})


def ml_model_create(request):
    if request.method == 'POST':
        form = MakeMLModelForm(request.POST)
        print(">> ML:create receive POST")
        print(form)
        print(request.FILES)
        # try:
        if form.is_valid():
            print(">>>> ML:create valid form")
            print(">>>> request.POST")
            print(request.POST)
            print(">>>> form.cleaned_data")
            print(form.cleaned_data)
            # post=ML_Model.objects.create(**form.cleaned_data)
            ml_model = form.save()
        else:
            print(">> Error")
            print(form.errors)
        #     pass
        # except Exception as e:
        #     print(e)
        return redirect ('ML:list')
    else:
        form = MakeMLModelForm()
        return render(request, 'ML/ml_model_form.html', {'form': form})
