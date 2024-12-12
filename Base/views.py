from django.shortcuts import render
from django.contrib import messages
from .models import Base_contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        # Validation
        if not (1 < len(name) < 30):
            messages.error(request, "Name length should be greater than 2 and less than 30 characters.")
            return render(request, 'home.html', {'name': name, 'email': email, 'phone': phone, 'content': content})
        
        if not (1 < len(email) < 30):
            messages.error(request, "Invalid email. Please try again.")
            return render(request, 'home.html', {'name': name, 'email': email, 'phone': phone, 'content': content})
        
        if not (1 < len(phone) < 15):
            messages.error(request, "Invalid phone number. Please try again.")
            return render(request, 'home.html', {'name': name, 'email': email, 'phone': phone, 'content': content})

        # Save the data if validation passes
        contact_entry = Base_contact(name=name, email=email, phone=phone, content=content)
        contact_entry.save()
        messages.success(request, "Thank you for contacting me! Your message has been saved.")
    
    return render(request, 'home.html')
