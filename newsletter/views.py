from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm

def newsletter_signup(request):
    form = NewsletterSignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up for our newsletter!')
            return redirect('newsletter_signup')
    else:
        form = NewsletterSignupForm()
    return render(request, 'newsletter/signup.html', {'form': form})
