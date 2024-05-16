from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField

# Constants --------------------------------------------------------- ##

# Constants for Post Model --------------------------- #
STATUS = (
    (0, 'Draft'),
    (1, 'Published')
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

# Constants for Location Model ----------------------- #
LOCATION = [
    ('AA', 'Arkenstone Avenue'),
    ('BB', 'Buckleberry Bend'),
    ('CC', 'Cobblestone Crossing'),
    ('EE', 'Elderberry End'),
    ('FF', 'Foxglove Field'),
    ('HH', 'Harvest Hollow'),
    ('MM', 'Marigold Mews'),
    ('OO', 'Old Oak End'),
    ('PP', 'Primrose Path'),
    ('RR', 'Redleaf Rise'),
    ('SS', 'Shirebrook Springs'),
    ('WW', 'Windrush Way'),
]

# Constants for Category Model ----------------------- #
CATEGORIES = [
    ('offers', 'Offers'),
    ('requests', 'Requests'),
]

# Constants for Subcategory Model -------------------- #
SUBCATEGORIES = [
    ('borrow', 'Borrow'),
    ('carpool', 'Carpool'),
    ('gardening', 'Gardening'),
    ('kids', 'Kids'),
    ('leisure', 'Leisure'),
    ('pets', 'Pets'),
    ('repairs', 'Repairs'),
    ('tech', 'Tech'),
    ('other', 'Other'),
]

# Models ------------------------------------------------------------ ##
class Location(models.Model):
    """
    Stores location for user posts.
    Related to :model:`Post`
    """
    location = models.CharField(max_length=50, choices=LOCATION)

    def __str__(self):
        return str(self.location)


class Category(models.Model):
    """
    Stores main categories for user posts.
    Related to :model:`Post`
    """
    category = models.CharField(max_length=8, choices=CATEGORIES)

    def __str__(self):
        return str(self.category)


class Subcategory(models.Model):
    """
    Stores subcategories for user posts.
    Related to :model:`Post`
    """
    subcategory = models.CharField(max_length=10, choices=SUBCATEGORIES)

    def __str__(self):
        return str(self.subcategory)


class Post(models.Model):
    """
    Stores a user post entry.
    Related to :model:`auth.User`
    and :model:`Comment`
    and :model:`Location`
    and :model:`Category`
    and :model:`Subcategory`.
    """
    author = models.ForeignKey(
        User, related_name='post_owner', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=60, null=False, blank=False)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)
    excerpt = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=5000, null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    location = models.ForeignKey(
        Location, related_name='post_location', null=True, blank=True, on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category, related_name='post_category', null=False, blank=False, on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        Subcategory, related_name='post_subcategory',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    post_image = CloudinaryField(
        'image', 
        transformation=[{'width': 400, 'crop': 'scale'}],
    )
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        null=True,
        blank=True,
    )
    tools_required = models.CharField(
        max_length=50,
        choices=TOOLS_REQUIRED,
        null=True,
        blank=True,
    )
    remarks = models.TextField(max_length=250, null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_post')
    bookmarks = models.ManyToManyField(User, related_name='bookmarked_post')

    class Meta:
        """
        Orders the posts in chronological order, newes first.
        """
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} | posted by {self.author}"


class Comment(models.Model):
    """
    Stores a user comment entry.
    Related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="commenter", on_delete=models.CASCADE)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    edited_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_comment')

    class Meta:
        """
        Orders the comments in chronological order, newes first.
        """
        ordering = ["published_date"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
