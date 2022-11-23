from django.contrib import admin

from ML.models import ML_Model


class ML_Admin(admin.ModelAdmin):
    list_display = [field.name for field in ML_Model._meta.fields]


admin.site.register(ML_Model, ML_Admin)

# class Graph_ML_Admin(admin.ModelAdmin):
