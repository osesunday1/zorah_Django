from .models import Surprises

def menu_links2(request):
    links2 = Surprises.objects.all()
    return dict(links2=links2)