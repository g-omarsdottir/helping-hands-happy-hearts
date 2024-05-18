from django.forms import ModelForm
from django import forms
from djrichtextfield.widgets import RichTextWidget
from cloudinary.forms import CloudinaryFileField
from .models import Post

# Check: Code from Cloudinary tutorial, implements a form on website. Check later if needed.
class PostForm(forms.ModelForm):
    """
    Form to create a post
    """

    class Meta:
        """
        Defines the form fields
        """
        model = Post
        fields = [
            'title', 'excerpt', 'content', 'status', 'location',
            'category', 'subcategory', 'post_image', 'availability',
            'tools_required', 'remarks', 'target_date',
        ]
        # excerpt = forms.CharField(widget=RichTextWidget())
        # content = forms.CharField(widget=RichTextWidget())
        widgets = {
            'excerpt': forms.RichTextWidget(),
            'content': forms.RichTextWidget(),
            'remarks': forms.Textarea(attrs={'rows': 5}),
        }

        labels = {
            'title': 'Post Title',
            'excerpt': 'Short Description',
            'content': 'Your Post Content',
            'status': 'Save as Draft or Publish Now',
            'location': 'Location',
            'category': 'Offer or Request',
            'subcategory': 'Subcategory',
            'post_image': 'Add Image',
            'availability': 'Availability',
            'tools_required': 'Tools Required',
            'remarks': 'Remarks',
            'target_date': 'Target Date',
        }


class PhotoForm(ModelForm):
    """
    Defines the form field for the image upload field.
    Specifies the formal handle file upload and utilizes Cloudinary for storage.
    Basic code structure from Cloudinary docs.
    Related to :model:`Post`
    """
    image = CloudinaryFileField(required=False)

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
