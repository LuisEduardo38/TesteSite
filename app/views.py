from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Livro, Autor, Genero, Video, Observacoes
from .forms import LoginForm, RegistroForm, livroForm, AutorForm, GeneroForm, ObservacoesForm, VideoForm
from django.contrib import messages

def home(request):
    dadosPagina = {'paginaAtiva': 'home'}
    return render(request, 'home.html', dadosPagina)


def livro(request):
    livros = Livro.objects.all()
    dadosPagina = {'paginaAtiva': 'livro', 'livros': livros}
    return render(request, 'livro.html', dadosPagina)


def autor(request):
    autores = Autor.objects.all()
    dadosPagina = {'paginaAtiva': 'autor', 'autores': autores}
    return render(request, 'autor.html', dadosPagina)


def contato(request):
    dadosPagina = {'paginaAtiva': 'contato'}
    return render(request, "contato.html", dadosPagina)


def resenha(request, id):
    livroEscolhido = get_object_or_404(Livro, id=id)
    dadosPagina = {'paginaAtiva': 'resenha', 'livroEscolhido': livroEscolhido}
    return render(request, 'resenha.html', dadosPagina)


def videoLivro(request, id):
    livroEscolhido = get_object_or_404(Livro, id=id)
    dadosPagina = {'paginaAtiva': 'video', 'livroEscolhido': livroEscolhido}
    return render(request, 'video.html', dadosPagina)


def autorResumo(request, id):
    autorEscolhido = get_object_or_404(Autor, id=id)
    dadosPagina = {'paginaAtiva': 'autorResumo', 'autorEscolhido': autorEscolhido}
    return render(request, 'autorResumo.html', dadosPagina)


# Métodos para seção de login

def login_views(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("secaoUsuario")
            else:
                form.add_error(None, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()

    dadosPagina = {'paginaAtiva': 'login', 'form': form}
    return render(request, "login.html", dadosPagina)


def registrar_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('login')
        else:
            messages.error(request, "Erro ao criar conta. Verifique os dados fornecidos.")
    else:
        form = RegistroForm()

    dadosPagina = {'paginaAtiva': 'Registra', 'form': form}
    return render(request, 'registrar.html', dadosPagina)


#@login_required
def secaoUsuario(request):
    dadosPagina = {'paginaAtiva' : 'secaoUsuario'}
    return render(request, 'secaoUsuario.html', dadosPagina)

def obter_modelo_form(tipo):
    if tipo == "livro":
        return Livro, livroForm
    elif tipo == "autor":
        return Autor, AutorForm
    elif tipo == "genero":
        return Genero, GeneroForm
    elif tipo == "observacoes":
        return Observacoes, ObservacoesForm
    elif tipo == "video":
        return Video, VideoForm
    else:
        raise ValueError("Tipo inválido")

def secaoCadastro(request, tipo):
    forms_map = {
        'livro': livroForm,
        'autor': AutorForm,
        'genero': GeneroForm,
        'observacao': ObservacoesForm,
        'video': VideoForm,
    }

    if tipo not in forms_map:
        messages.error(request, "Tipo de cadastro inválido.")
        return redirect("secaoCadastro")

    FormClass = forms_map[tipo]
    titulo = tipo.capitalize()

    if request.method == "POST":
        form = FormClass(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{titulo} salvo com sucesso!")
            return redirect("secaoUsuario")
        else:
            messages.error(request, f"Erro ao salvar {titulo}. Verifique os campos.")
    else:
        form = FormClass()

    dadosPagina = {'paginaAtiva' : 'secaoCadastro', 'form': form, 'titulo': titulo}
    return render(request, "secaoCadastro.html", dadosPagina)

def listaObjetos(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "listaObjetos.html", dadosPagina)

def listaObjetosEditar(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "listaObjetosEditar.html", dadosPagina)

def listaObjetosApagar(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "listaObjetosApagar.html", dadosPagina)

def listaObjetosApagarAutor(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "listaObjetosApagarAutor.html", dadosPagina)

def secaoGenerica(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "secaoGenerica.html", dadosPagina)

def secaoGenerica02(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "secaoGenerica02.html", dadosPagina)

def secaoGenericaVideo(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "secaoGenericaVideo.html", dadosPagina)

def secaoGenericaVideo02(request, tipo):
    modelo, _ = obter_modelo_form(tipo)
    objetos = modelo.objects.all()
    titulo = tipo.capitalize()
    
    dadosPagina = {
        'paginaAtiva': 'listaObjetos',
        'titulo' : titulo,
        'tipo': tipo,
        'objetos': objetos,
    }
    return render(request, "secaoGenericaVideo02.html", dadosPagina)

def secaoEditar(request, tipo, pk):
    modelo, form_classe = obter_modelo_form(tipo)
    objeto = get_object_or_404(modelo, pk=pk)

    if request.method == "POST":
        form = form_classe(request.POST, request.FILES, instance=objeto)
        if form.is_valid():
            form.save()
            messages.success(request, f"{tipo.capitalize()} editado com sucesso!")
            return redirect("secaoUsuario")
        else:
            messages.error(request, "Erro ao salvar. Verifique os campos.")
    else:
        form = form_classe(instance=objeto)

    dadosPagina = {
        'paginaAtiva': 'editar_objeto',
        'form': form,
        'titulo': f"Editar {tipo.capitalize()}",
    }
    return render(request, "secaoCadastro.html", dadosPagina)

def secaoApagar(request, tipo, pk):
    modelo, _ = obter_modelo_form(tipo)
    objeto = get_object_or_404(modelo, pk=pk)

    if request.method == "POST":
        objeto.delete()
        messages.success(request, f"{tipo.capitalize()} apagado com sucesso!")
        return redirect("secaoUsuario")

    dadosPagina = {
        'paginaAtiva': 'apagar_objeto',
        'titulo': f"Apagar {tipo.capitalize()}",
        'objeto': objeto,
    }
    return render(request, "secaoComfirmacao.html", dadosPagina)