from django.shortcuts import render

def home(request):
    return render(request, "gestioncursos.html")

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")
