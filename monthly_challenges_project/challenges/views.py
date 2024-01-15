from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string           # importing to read html files, converts to a string

# Create your views here.

monthly_challenges_dict = {
    "january": "Hi , Milana you are in January month",
    "february": "Hi , you are in January month",
    "march": "Hi , you are in January month",
    "april": "Hi , you are in april month",
    "may": "Hi , you are in may, Milana is here month",
    "june": "Hi , you are in june month",
    "july": "Hi , you are in july month",
    "august": "Hi , you are in august month",
    "september": "Hi , you are in september month",
    "october": "Hi , you are in october month",
    "november": "Hi , you are in november month",
    "december": None
}


def months_index(request):
    # list_months = ""   # creating an empty string to use it later
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/months_index.html", {
        "months": months
    })

#     for month in months:    # looping through the all months
#         capitalized_month = month.capitalize()
#         month_path = reverse("month-challenge", args=[month])  # it's a path
#         list_months += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
# # loop through all the month and generates a new string
#     response_data = f"<ul>{list_months}</ul>"   # unordered list
#     return HttpResponse(response_data)


def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges_dict.keys())    # taking dict keys(only months) and convert it to a list
    if month > len(months):    # month len would be 12, if that is more then will return not found msg
        return HttpResponseNotFound('Invalid number of the month!')
    redirect_month = months[month - 1]    # then taking from a list by index, it starts from 0, that why - 1
    redirect_path = reverse("month-challenge", args=[redirect_month])   # creating url path by referring name created in urls files name="month-challenge"
    # what it does - it knows how to redirect by using name, adding args=in list format
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request,"challenges/challenge.html", {
            "name_of_the_month": month,
            "monthly_text": challenge_text         # step 1 , create a dict with a key and pass a parameter
        })      # replacing  response_data = render_to_string('challenges/challenge.html') by render   # response_data = render_to_string('challenges/challenge.html')   # pass location of html         # f"<h1>{
    except:
        raise Http404("From 404 - Not found")

