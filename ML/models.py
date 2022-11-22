from django.db import models

# Create your models here.
class ML_Model(models.Model):
    title=models.CharField('TITLE', max_length=20)
    version=models.FloatField('VERSION')
    is_selected=models.BooleanField('IS_SELECTED')
    date_published = models.DateField('DATE_PUBLISHED', auto_now_add=True) 
    
    # 자동정렬할거면    
    # class Meta:
    #     ordering = ('')

    def __str__(self):
        return self.title