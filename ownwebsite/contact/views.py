from django.shortcuts import render
from .forms import MsgForm
from .models import Msg
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect


def contact(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MsgForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            tem = Msg()
            tem.msg_subject = form.cleaned_data['msg_subject']
            tem.msg_text = form.cleaned_data['msg_text']
            tem.user_name = form.cleaned_data['user_name']
            tem.user_email = form.cleaned_data['user_email']
            tem.save()
            messages.info(request, 'Your Message has been Successfully Submitted.')
            recipients = ['k.surajraj9@gmail.com']
            # print('before sending email')
            send_mail((tem.user_name + ' : ' + tem.user_email + ' : ' + tem.msg_subject), tem.msg_text,
                      'lykira2468@gmail.com', recipients, fail_silently=False)
            # print('email sent')
            # redirect to a new URL:
            return HttpResponseRedirect('/contact/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MsgForm()

    return render(request, 'contact.html', {'form': form})
