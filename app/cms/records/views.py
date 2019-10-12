from django.shortcuts import render
from .models import Doctor, Patient, Contact

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    contacts = Contact.objects.all()
    context = {
        'doctors': doctors,
        'patients': patients,
        'contacts': contacts,
    }
    return render(request, 'records/index.html', context)
