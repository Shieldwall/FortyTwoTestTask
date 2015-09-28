from django.shortcuts import get_object_or_404, render

from .models import User


def index(request):
    info = get_object_or_404(User, pk=1)
    return render(request, 'hello/index.html', {'user': info})
