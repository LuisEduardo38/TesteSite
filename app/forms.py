from django import forms
from .models import Livro, Autor, Genero, Observacoes, Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário'})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    
class livroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            "capa",
            "titulo",
            "autor",
            "generoLivro",
            "lancamento",
            "nota",
            "observacao",
            "resumo",
            "introducao",
            "desenvolvimento",
            "conclusao",
            "imagem01",
            "imagem02",
            "videos",
        ]

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            "imagem",
            "nome",
            "naturalidade",
            "nascimento",
            "generoAutor",
            "publicoAlvo",
            "editora",
            "resumo",
            "capaMaisLido01",
            "capaMaisLido02",
            "capaMaisLido03",
            "maisLido",
            "livros",
        ]

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ["descricao"]

class ObservacoesForm(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = ["descricao"]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["tituloVideo", "urlVideo"]