from .forms import RideForm, NewRideForm


from django.shortcuts import render, redirect # type: ignore
import os
from .models import Person
from django.shortcuts import render

# relative import of forms
# from .forms import RideForm

# Create your views here.

def index(request):

  context = {}

  if "search" in request.GET:
    search = request.GET["search"]

    context["people"] = Person.objects.filter(
        origination__icontains=search) | Person.objects.filter( destination_state__icontains=search) | Person.objects.filter( destination_state__icontains=search)


  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()

  return render(request, "index_view.html", context)


def create(request):

  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()

  return redirect("/rides")

def form(request):
  context = {}
  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  return render(request, "form.html", context)


from transformers import pipeline
from .models import Person
def ai_interaction(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        rides_data = Person.objects.all()
        system_message = f"You are trying to help folks get rides based on the data you have in your database: {rides_data}"
        prompt = f"{system_message} {user_input} AI:"
        generator = pipeline("text-generation", model="openai-community/gpt2")
        ai_text = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
        final_ai_text = ai_text.split("AI:")[-1].strip()
        return render(request, 'index_view.html', {'ai_text': final_ai_text})
    return render(request, 'index_view.html')
