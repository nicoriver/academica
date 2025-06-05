from django.shortcuts import render, redirect
from .models import Usuario, PlanEstudio
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")
def update(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('mail') and request.POST.get('telefono') and request.POST.get('FechaNac'):
           user_id_old = request.POST.get('id')
           user_old = Usuario.objects.get(id = user_id_old)
           user = Usuario()  
           user.id  = request.POST.get('id')       
           user.nombre = request.POST.get('nombre')
           user.apellido = request.POST.get('apellido')
           user.correo = request.POST.get('mail')
           user.telefono = request.POST.get('telefono')
           user.f_nac = request.POST.get('FechaNac')
           user.f_registro = user_old.f_registro
           user.save()
           return redirect('list')

    else:
        users = Usuario.objects.all()
        datos = {'usuarios' : users}
        return render(request, "crud_usuarios/update.html", datos)

def list(request):
    users = Usuario.objects.all()
    datos = {'usuarios' : users}
    return render(request, "crud_usuarios/list.html", datos)

def delete(request):
    if request.method == 'POST':
       if request.POST.get('id'):
           id_a_borrar = request.POST.get('id')
           tupla = Usuario.objects.get(id = id_a_borrar)
           tupla.delete()
           return redirect('list')
    else:
        users = Usuario.objects.all()
        datos = {'usuarios' : users}
        return render(request, "crud_usuarios/delete.html", datos)

def add(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('mail') and request.POST.get('telefono') and request.POST.get('FechaNac'):
            user = Usuario()           
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('mail')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('FechaNac')
            user.save()
            return redirect('list')
        else:
            # Mostrar el mismo formulario con un mensaje de error
            return render(request, "crud_usuarios/add.html", {
                'error': 'Todos los campos son obligatorios.'
            })
    else:
        return render(request, "crud_usuarios/add.html")


#modelo de plan de estudio

def listplan(request):
    planes = PlanEstudio.objects.all()
    datos = {'planes' : planes}
    return render(request, "crud_planestudios/list.html", datos)