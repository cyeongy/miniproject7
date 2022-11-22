from django.test import TestCase
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from .models import ML_Model
from django.conf import settings
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.

class Test_ML_Model(TestCase):

    def setUp(self):
        my_model = ML_Model()
        my_model.name = 'test_model'

        my_model.file = SimpleUploadedFile(
            "test_cnn_model.h5",
            b"cnn_model_binary_code"  # note the b in front of the string [bytes]
        )

        my_model.save()

    def test_Create_model(self):
        test = ML_Model.objects.get(name='test_model')
        self.assertEqual(test.name, 'test_model')
        print(test.created)
        print(test.file.path)
        print(test.file)
=======

# Create your tests here.
>>>>>>> eb2fa32 (Rebase commit)
