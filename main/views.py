from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306274964',
        'name': 'Kaindra Rizq Sachio',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)