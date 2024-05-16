from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField

# Constants for Post Model
STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

AVAILABILITY_CHOICES = [
    ('evenings', 'Evenings'),
    ('weekends', 'Weekends'),
    ('generally', 'Generally Available'),
]

TOOLS_REQUIRED = [
    ('have', 'I Have the Necessary Tools'),
    ('need', 'Tools Required - which I Do Not Have'),
    ('n.a.', 'No Tools Required'),
]

# Create your models here.
class Post(models.Model):
    """
    A model to store and manage post entries.
    Related to :model:`auth.User`
    and :model:`Location`
    and :model:`Category`
    and :model:`Subcategory`.
    """
    author = models.ForeignKey(
        User, related_name="post_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=60, null=False, blank=False)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)
    excerpt = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=5000, null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    location = models.ForeignKey(
        Location, related_name="location", null=True, blank=True, on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category, related_name="category", null=False, blank=False, on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        Subcategory, related_name="subcategory", null=True, blank=True, on_delete=models.SET_NULL
    )
    post_image = CloudinaryField(
        'image', 
        transformation=[{'width': 400, 'crop': 'scale'}],
        options={
            'quality': 75,
            'fetch_format': 'webp',
            'folder': 'post-images'
        }
    )
    availability = models.CharField(
        max_length=9,
        choices=AVAILABILITY_CHOICES,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    tools_required = models.CharField(
        choices=TOOLS_REQUIRED,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    remarks = models.TextField(max_length=250, null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="user_post")

    class Meta:
        """
        Orders the posts in chronolical order, newes first.
        """
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
