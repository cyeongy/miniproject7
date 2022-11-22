from django.db import models

# Create your models here.
class ML_Model(models.Model):
    title=models.CharField('TITLE', max_length=20)
    version=models.FloatField('VERSION', default=1.0)
    is_selected=models.BooleanField('IS_SELECTED', default=False)
    date_published = models.DateField('DATE_PUBLISHED', auto_now_add=True) 
    file = models.FileField(upload_to='models/')
    # 자동정렬할거면    
    # class Meta:
    #     ordering = ('')

    def __str__(self):
        return self.title