from django.shortcuts import render, redirect
from .models import Usuario
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")
def update(request):
    return render(request, "crud_usuarios/update.html")

def list(request):
    users = Usuario.objects.all()
    datos = {'usuarios' : users}
    return render(request, "crud_usuarios/list.html", datos)

def delete(request):
    return render(request, "crud_usuarios/delete.html")

def add(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_nac'):
            user = Usuario()           
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()
            return redirect('listar')
        else:
            # Mostrar el mismo formulario con un mensaje de error
            return render(request, "crud_usuarios/add.html", {
                'error': 'Todos los campos son obligatorios.'
            })
    else:
        return render(request, "crud_usuarios/add.html")


