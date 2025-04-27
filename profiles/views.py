"""Views for the profiles app."""


from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet
# consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """View to display the list of all profiles."""

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)
    

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis
# pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """View to display the details of a specific profile."""
    
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        context = {'username': username}
        return render(request, 'profiles/profile_404.html', context, status=404)
