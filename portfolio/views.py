from django.shortcuts import render
from . forms import TestimonialForm
from . models import Testimonial




# Create your views here.

def home(request):
    template = 'index.html'

    return render(request, template)

def portfolio(request):
    template = 'portfolio.html'

    return render(request, template)

def contacts(request):
    template = 'contacts.html'

    return render(request, template)

def services(request):
    template = 'services.html'

    return render(request, template)

def testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TestimonialForm()
    
    update = Testimonial.objects.all()
    context = {'form':form, 'update':update}
    template = 'testimonial.html'

    return render(request, template, context)


def blog(request):
    template = 'blog.html'

    return render(request, template)

def pricing(request):
    template = 'pricing.html'

    return render(request, template)

def FAQs(request):
    template = 'FAQs.html'

    return render(request, template)