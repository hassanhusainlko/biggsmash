from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            form = ContactForm()
    else:
        form = ContactForm()
    
    return render(request, 'contact/index.html', {'form': form})
