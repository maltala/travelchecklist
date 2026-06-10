from django.shortcuts import render  # Ayuda para devolver HTML renderizado con un template

# Create your views here.


def home(request):
    # Renderiza la plantilla de inicio y la devuelve como respuesta HTTP
    return render(request, 'trips/home.html')

