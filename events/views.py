from django.shortcuts import render
from .models import Registration


# HOME PAGE
def home(request):
    return render(request, "home.html")


# REGISTRATION PAGE
def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        sem = request.POST.get("semester")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        event = request.POST.get("event")

        team_name = request.POST.get("team_name")
        player2 = request.POST.get("player2")
        player3 = request.POST.get("player3")
        player4 = request.POST.get("player4")

        payment_method = request.POST.get("payment_method")
        transaction_id = request.POST.get("transaction_id")

        screenshot = request.FILES.get("payment_screenshot")

        # PAYMENT VALIDATION

        if payment_method == "UPI":
            if not transaction_id and not screenshot:
                return render(request, "register.html", {
                    "error": "For UPI payment please enter Transaction ID or upload screenshot."
                })

        if payment_method == "Screenshot":
            if not screenshot:
                return render(request, "register.html", {
                    "error": "Please upload payment screenshot."
                })

        # SAVE DATA

        Registration.objects.create(
            participant_name=name,
            semester_department=sem,
            contact_number=contact,
            email=email,
            event_name=event,

            team_name=team_name,
            player2=player2,
            player3=player3,
            player4=player4,

            payment_method=payment_method,
            transaction_id=transaction_id,
            payment_screenshot=screenshot
        )

        return render(request, "success.html")

    return render(request, "register.html")