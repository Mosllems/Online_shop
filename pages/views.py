from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from .forms import MessageForm

class HomePageView(generic.TemplateView):
    template_name = "home.html"



def contact_us(request):
    if request.method == "POST":
        message_obj = MessageForm(request.POST)
        if message_obj.is_valid():
            message_obj = message_obj.save(commit=False)
            message_obj.user = request.user
            message_obj.email = request.user.email
            message_obj.save()
            messages.success(request, _("Your message has been sent"))
            # return redirect('contactus')


    return render(request, "pages/contactus.html")

