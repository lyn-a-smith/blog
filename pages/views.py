from django.http import HttpResponse
from django.shortcuts import render
from  django.views.generic import TemplateView

# Create your views here.
# Function Based View vs. Class Based View

# Class Based View
class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs): # **kwargs allows you to pass any number of keyword arguments to the function. It collects them into a dictionary.
        context = super().get_context_data(**kwargs)
        context['name'] = "Lyn"
        context['address'] = "123 Main St, Anytown, USA"
        context['email'] = "lyn@example.com"
        return context

# Function Based View
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    contact_info = {
        "name": "Lyn",
        "address": "123 Main St, Anytown, USA",
        "email": "lyn@example.com",
    }

    return render(request, "pages/contact.html", contact_info)
