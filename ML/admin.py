from django.contrib import admin
from ML.models import ML_Model, Evaluation
## 안쓰는 모듈 지우기
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
##

class ML_Admin(admin.ModelAdmin):
    list_display = [field.name for field in ML_Model._meta.fields] 
    
    def changelist_view(self, request, extra_context=None):
        # QuerySet
        chart_data = (
            ML_Model.objects.all().values('title', 'version').order_by('title')        
        )   
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>       ", end='')
        print(chart_data)        
        
        # data = ML_Model.objects.all()
        # as_json = json.dumps(list(data), cls=DjangoJSONEncoder)
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

        
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)

class Evaluation_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Evaluation._meta.fields]
    
    def changelist_view(self, request, extra_context=None):
        # QuerySet
        chart_data = (
            Evaluation.objects.all().values('ml_model', 'total', 'success').order_by('ml_model')        
        )   
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>       ", end='')
        print(chart_data)        
        
        # data = ML_Model.objects.all()
        # as_json = json.dumps(list(data), cls=DjangoJSONEncoder)
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

        
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(ML_Model, ML_Admin)
admin.site.register(Evaluation, Evaluation_Admin)
