from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from .models import ML_Model
from django.conf import settings
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

import mock
import shutil
import tempfile

# Create your tests here.
MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class Test_ML_Model(TestCase):

    def setUp(self):
        my_model = ML_Model()
        my_model.title = 'test_model'
        # my_model.version = 1.0
        # my_model.is_selected = True
        test_mock = mock.MagicMock(spec=File)
        test_mock.name = 'test_model.h5'
        my_model.file = test_mock
        my_model.save()

    @classmethod
    def tearDownClass(cls):
        def tearDownClass(cls):
            shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
            super().tearDownClass()

    def test_Create_model(self):
        test = ML_Model.objects.get(title='test_model')
        print(test.id)
        print(test.date_published)
        print(test.file.path)
        print(test.file)
