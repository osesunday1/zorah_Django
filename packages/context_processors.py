from .models import Packages

def menu_links1(request):
    links1 = Packages.objects.all()
    return dict(links1=links1)