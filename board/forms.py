from django.forms import ModelForm
from .models import Post

class PhotoForm(ModelForm):
    """
    Defines the form field for the image upload field.
    Specifies the formal handle file upload and utilizes Cloudinary for storage. 
    Related to :model:`Post`
    """
    image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].options={
            'quality': 75,
            'fetch_format': 'webp',
            'folder': 'post-images'
    }
