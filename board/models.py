from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField

# Variables
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    A model to store and manage post entries.
    Related to :model:`auth.User`.
    """
    author = models.ForeignKey(User, related_name="post_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)
    excerpt = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=5000, null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = CloudinaryField(
        'image', 
        transformation=[{'width': 400, 'crop': 'scale'}],
        options={'quality': 75, 'fetch_format': 'webp'})
