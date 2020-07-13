from django.forms import ModelForm
from . import models

class UploadForm(ModelForm):
    class Meta:
        model = models.UserFile
        fields = ['filename', 'file', 'estimation']
        labels = {
            "estimation": "Estimation (Days)"
        }

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')
            super(UploadForm, self).__init__(*args, **kwargs)
