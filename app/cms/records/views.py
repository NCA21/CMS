from django.shortcuts import render
from .models import It, Nit, Nurses

# Create your views here.
def index(request):
    it = It.objects.all()
    nit = Nit.objects.all()
    nurses = Nurses.objects.all()
    system = {
        'it': it,
        'nit': nit,
        'nurses': nurses,
    }
    return render(request, 'records/index.html', system)
