from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from ML.models import ML_Model

admin.site.register(ML_Model)

# @admin.register(ML_Model)
# class MLModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'version', 'is_selected', 'date_published')

#     def tag_list(self, obj):
#         return ','.join([t.name for t in obj.tags.all()])

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')
>>>>>>> eb2fa32 (Rebase commit)
