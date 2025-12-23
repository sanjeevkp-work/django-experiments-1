from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Avoid eating dairy food in January!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat Django for at least 20 minutes every day!",
    "may": "Play football for at least 20 minutes every day!",
    "june": "June Django for at least 20 minutes every day!",
    "july": "July Django for at least 20 minutes every day!",
    "august": "August Eat Django for at least 20 minutes every day!",
    "september": "September Play football for at least 20 minutes every day!",
    "october": "October Eat Django for at least 20 minutes every day!",
    "november": "November Django for at least 20 minutes every day!",
    "december": None,  # "December Eat Django for at least 20 minutes every day!",
}


def index(request):
    months = list[str](monthly_challenges.keys())
    # for month in months:
    #     redirect_path = reverse("monthly-challenge", args=[month])
    #     list_items += f'<li><a href="{redirect_path}">{month.capitalize()}</a></li>'
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )


def monthly_challenge_by_number(request, month):
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month!")
    else:
        string_month = list[str](monthly_challenges.keys())[month - 1]
        redirect_path = reverse("monthly-challenge", args=[string_month])
        return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    if month.lower() in monthly_challenges:
        challenge_text = monthly_challenges[month.lower()]
        return render(
            request,
            "challenges/challenge.html",
            {
                "text": challenge_text,
                "month_name": month.capitalize(),
            },
        )
    else:
        raise Http404()
