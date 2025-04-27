"""Views for the lettings app."""

from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa.
# Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum 
# primis in faucibus orci luctus et ultrices 
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """View to display the list of all lettings."""
    lettings_list = Letting.objects.all()
    logger.info("Displayed the list of all lettings.")
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu
# consequat pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac
# condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis 
# urna pellentesque justo mattis ullamcorper ac non tellus. In 
# tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor 
# risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. 
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """View to display the details of a specific letting."""
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Displayed details for letting id {letting_id}.")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.warning(f"Letting with id {letting_id} not found.")
        context = {'letting_id': letting_id}
        return render(request, 'lettings/letting_404.html', context, status=404)
