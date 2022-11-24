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
    return render(request, 'ml/list.html', {'model_all': model_list})


def ml_model_create(request):
    if request.method == 'POST':
        form = MakeMLModelForm(request.POST)
        # try:
        if form.is_valid():
            ml_model = form.save()
        else:
            print(">> Error")
            print(form.errors)

        return redirect ('ml:list')
    else:
        form = MakeMLModelForm()
        return render(request, 'ml/ml_model_form.html', {'form': form})
