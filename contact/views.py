from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to a "thank you" page or display a success message
    else:
        form = ContactForm()
    context = {'form': form}  # Include the form in the context dictionary
    return render(request, 'contact/contact.html', context)
