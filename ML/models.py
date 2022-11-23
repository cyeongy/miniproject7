from django.db import models


# Create your models here.
class ML_Model(models.Model):
    title = models.CharField('TITLE', max_length=20)
    version = models.FloatField('VERSION', default=1.0)
    is_selected = models.BooleanField('IS_SELECTED', default=False)
    date_published = models.DateField('DATE_PUBLISHED', auto_now_add=True)
    model_file = models.FileField('MODEL_FILE', upload_to='models/')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

    def save(self, * args, ** kwargs):
        # print(">> save method")
        # for k, v in kwargs.items():
        #     print(k, v)
        if self.is_selected:
            # print(ML_Model.objects.filter(is_selected=True))
            ML_Model.objects.filter(is_selected=True).update(is_selected=False)

        super().save(* args, ** kwargs)


class Evaluation(models.Model):
    ml_model = models.OneToOneField(to=ML_Model, on_delete=models.CASCADE)
    total = models.IntegerField('TOTAL', default=0)
    success = models.IntegerField('SUCCESS', default=0)