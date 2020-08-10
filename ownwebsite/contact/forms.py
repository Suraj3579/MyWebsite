from django import forms

class MsgForm(forms.Form):
    user_name = forms.CharField(max_length=30, help_text='Your Name', widget=forms.TextInput(attrs={"class":'form-control vis_field', "placeholder": 'Name'}))
    user_email = forms.CharField(max_length=254, help_text='Your Email Address', widget=forms.TextInput(attrs={"class":'form-control vis_field', "placeholder": 'Email Address'}))
    msg_subject = forms.CharField(max_length=300, help_text='Enter Subject', widget=forms.TextInput(attrs={"class":'form-control vis_field', "placeholder": 'Subject'}))
    msg_text = forms.CharField(max_length=1000, help_text='Enter Message here', widget=forms.Textarea(attrs={"class":'form-control vis_field', "placeholder": 'Type Your Message Here', "row": '3'}))
