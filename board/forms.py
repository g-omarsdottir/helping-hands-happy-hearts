from django import forms
from django.forms import ModelForm

# from djrichtextfield.widgets import RichTextWidget
from ckeditor.fields import RichTextField
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form to create a post.
    Related to :model:`board.Post`.
    ***Template:***
    :template:`board/add_post.html`
    """

    content = RichTextField()

    class Meta:
        """
        Defines the form fields
        """

        model = Post
        fields = [
            "title",
            "excerpt",
            "content",
            "status",
            "location",
            "category",
            "subcategory",
            "post_image",
            "availability",
            "tools_required",
            "remarks",
            "contact_details",
            "target_date",
        ]
        # excerpt = forms.CharField(widget=RichTextWidget())
        # content = forms.CharField(widget=RichTextWidget())
        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 5}),
            "remarks": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Post Title",
            "excerpt": "Short Description",
            "content": "Your Post Content",
            "status": "Save as Draft or Publish Now",
            "location": "Location",
            "category": "Offer or Request",
            "subcategory": "Subcategory",
            "post_image": "Add Image",
            "availability": "Availability",
            "tools_required": "Tools Required",
            "remarks": "Remarks",
            "contact_details": "Contact Details (Email or Phone)",
            "target_date": "Target Date",
        }


class CommentForm(forms.ModelForm):
    """
    Form to create a comment on a post.
    Related to :model:`board.Comment`
    and :model:`board.Post`.
    ***Template:***
    :template:`board/post_detail.html`
    """

    class Meta:
        """
        Defines the form fields
        """

        model = Comment
        fields = [
            "body",
        ]
