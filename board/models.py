from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# Constants for Post Model --------------------------- #
STATUS = ((0, "Draft"), (1, "Published"))

AVAILABILITY_CHOICES = [
    ("Evenings", "Evenings"),
    ("Weekends", "Weekends"),
    ("Generally Available", "Generally Available"),
]

TOOLS_REQUIRED = [
    ("I Have the Necessary Tools", "I Have the Necessary Tools"),
    ("Tools Required - which I Do Not Have",
        "Tools Required - which I Do Not Have"),
    ("No Tools Required", "No Tools Required"),
]


# Models ------------------------------------------------------------ ##
class Location(models.Model):
    """
    Stores location for user posts.
    Related to :model:`Post`
    """

    LOCATION = [
        ("AA", "Arkenstone Avenue"),
        ("BB", "Buckleberry Bend"),
        ("CC", "Cobblestone Crossing"),
        ("EE", "Elderberry End"),
        ("FF", "Foxglove Field"),
        ("HH", "Harvest Hollow"),
        ("MM", "Marigold Mews"),
        ("OO", "Old Oak End"),
        ("PP", "Primrose Path"),
        ("RR", "Redleaf Rise"),
        ("SS", "Shirebrook Springs"),
        ("WW", "Windrush Way"),
    ]
    location = models.CharField(max_length=50, choices=LOCATION)

    def __str__(self):
        return (
            self.get_location_display()
        )  # get_location_display returns "human-readable" value


class Category(models.Model):
    """
    Stores main categories for user posts.
    Related to :model:`Post`
    """

    CATEGORIES = [
        ("offers", "Offers"),
        ("requests", "Requests"),
    ]
    category = models.CharField(max_length=8, choices=CATEGORIES)

    def __str__(self):
        return (
            self.get_category_display()
        )  # get_category_display returns "human-readable" value


class Subcategory(models.Model):
    """
    Stores subcategories for user posts.
    Related to :model:`Post`
    """

    SUBCATEGORIES = [
        ("borrow", "Borrow"),
        ("carpool", "Carpool"),
        ("gardening", "Gardening"),
        ("kids", "Kids"),
        ("leisure", "Leisure"),
        ("pets", "Pets"),
        ("repairs", "Repairs"),
        ("tech", "Tech"),
        ("other", "Other"),
    ]
    subcategory = models.CharField(max_length=10, choices=SUBCATEGORIES)

    def __str__(self):
        return (
            self.get_subcategory_display()
        )  # get_subcategory_display returns "human-readable" value


class Post(models.Model):
    """
    Stores a user post entry.
    Related to :model:`auth.User`
    and :model:`Location`
    and :model:`Category`
    and :model:`Subcategory`.
    """

    author = models.ForeignKey(
        User, related_name="post_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=40, null=False, blank=False)
    slug = AutoSlugField(
        populate_from="title", always_update=True, unique=True
    )
    excerpt = models.CharField(max_length=100, null=False, blank=False)
    content = RichTextField(max_length=5000, null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    location = models.ForeignKey(
        Location,
        related_name="post_location",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey(
        Category,
        related_name="post_category",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    subcategory = models.ForeignKey(
        Subcategory,
        related_name="post_subcategory",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    post_image = ResizedImageField(
        size=[400, None],
        upload_to="happyhelping/",
        null=True,
        blank=True,
        quality=75,
        force_format="webp",
    )
    availability = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, null=True, blank=True
    )
    tools_required = models.CharField(
        max_length=50, choices=TOOLS_REQUIRED, null=True, blank=True
    )
    remarks = models.TextField(max_length=250, null=True, blank=True)
    contact_details = models.CharField(max_length=250, null=False, blank=False)
    target_date = models.DateField(null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_post")

    def total_likes(self):
        """
        Direct access to number of total likes.
        Related to :view:`PostDetail`
        **Template:**:
        :template:`post_detail.html`
        """
        return self.likes.count()

    class Meta:
        """
        Orders the posts in chronological order, newest first.
        """

        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} | posted by {self.author}"
