from django.shortcuts import render

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")
def update(request):
    return render(request, "crud_usuarios/update.html")

def list(request):
    return render(request, "crud_usuarios/list.html")

def delete(request):
    return render(request, "crud_usuarios/delete.html")

def add(request):
    return render(request, "crud_usuarios/add.html")


