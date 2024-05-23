from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Location, Category, Subcategory


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Fields to display and search by in admin panel.
    Summernote for user-friendly rich-text editor.
    """

    list_display = (
        "author",
        "title",
        "slug",
        "status",
        "published_date",
        "location",
        "category",
        "subcategory",
    )
    list_filter = ("author", "published_date", "category", "subcategory", "location")
    summernote_fields = "content"


admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Comment)
