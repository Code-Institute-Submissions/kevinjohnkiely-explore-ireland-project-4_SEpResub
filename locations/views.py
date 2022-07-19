from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Location


class LocationList(generic.ListView):
    model = Location
    queryset = Location.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 6

class LocationSingle(View):

    def get(self, request, location_slug, *args, **kwargs):
        queryset = Location.objects.filter(status=1)
        location = get_object_or_404(queryset, slug=location_slug)
        comments = location.comments.filter(comment_approved=True).order_by('created_at')
        post_liked = False
        if location.likes.filter(id=self.request.user.id).exists():
            post_liked = True

        return render(
            request,
            "location_single.html",
            {
                "location": location,
                "comments": comments,
                "liked": post_liked
            }
        )