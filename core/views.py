from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from core.models import Product
from core.forms import ProductForm


def productos_view(request):
    # Obtener todos los productos de la base de datos
    productos = Product.objects.all()

    # Imprimir los datos de todos los productos (solo para fines de depuración)
    # for producto in productos:
    #    print("Título:", producto.title)
    #    print("Categoría:", producto.category)
    #    print("Imagen destacada:", producto.featured_image)
    #    print("Descripción:", producto.description)
    #    print("Imágenes adicionales:", producto.additional_images)

    # Pasar todos los productos al contexto de la plantilla
    #return render(request, 'dashboard/productos.html', {"productos": productos})

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES para manejar archivos
        if form.is_valid():
            form.save()  # Esto guardará los datos en la base de datos
            return redirect('productos')  # Redirige a la página de productos después de crear uno
    else:
        form = ProductForm()
    return render(request, 'dashboard/productos.html', {'productos': productos, 'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('login')

def error_404(request, exception):
    return render(request, 'error/404.html', status=404)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard/base.html')