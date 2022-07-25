from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
REGION_OPTIONS = (
    ('Connaught','Connaught'),
    ('Leinster', 'Leinster'),
    ('Munster','Munster'),
    ('Ulster','Ulster'),
)

class Location(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="location_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    region = models.CharField(max_length=20, choices=REGION_OPTIONS, blank=True)
    body = models.TextField()
    location_image = CloudinaryField('image', default='placeholder_image')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='location_likes', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('my_locations')


class Comment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    # comment_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
