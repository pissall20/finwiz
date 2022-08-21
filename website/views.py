from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import Team, Service, FAQ


# Create your views here.
def index(request):
    team = Team.objects.all().order_by("order")
    services = Service.objects.all().order_by("order")
    faq = FAQ.objects.all().order_by("order")
    contact_form = ContactForm()

    context = {
        "contact_form": contact_form,
        "team": team,
        "services": services,
        "faqs": faq
    }
    return render(request, 'website/index.html', context)


def inner_page(request):
    return render(request, 'website/inner-page.html', {})


def privacy(request):
    context = {}
    return render(request, 'website/privacy-policy.html', context)


def disclaimer(request):
    context = {}
    return render(request, 'website/disclaimer.html', context)


def about(request):
    context = {}
    return render(request, 'website/about.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            print(form.cleaned_data)
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            form.save()

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return HttpResponse("Your query has been sent.", status=200)
            return HttpResponse("Message sent successfully", status=200)

    form = ContactForm()
    return render(request, 'aiprizm/index.html', {'form': form})
