from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import home, livro, autor, contato, resenha, videoLivro, autorResumo, login_views, registrar_view, secaoGenericaVideo02, secaoUsuario, secaoCadastro, secaoEditar, secaoApagar, listaObjetos, listaObjetosApagar, listaObjetosEditar, secaoGenerica, secaoGenericaVideo, listaObjetosApagarAutor, secaoGenerica02


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('livro', livro, name="livro"),
    path('autor/', autor, name="autor"),
    path('contato/', contato, name="contato"),
    path('livro/resenha/<int:id>', resenha, name="resenha"),
    path('livro/video/<int:id>', videoLivro, name="videoLivro"),
    path('autor/autorResumo/<int:id>', autorResumo, name="autorResumo"),
    path('login/', login_views, name="login"),
    path('registrar/', registrar_view, name="registrar"),
    path('secaoUsuario/', secaoUsuario, name="secaoUsuario"),
    path('secaoUsuario/secaoCadastro/<str:tipo>', secaoCadastro, name="secaoCadastro"),
    path('secaoUsuario/listaObjetos/<str:tipo>', listaObjetos, name="listaObjetos"),
    path('secaoUsuario/secaoEditar/<str:tipo>/<int:pk>/', secaoEditar, name="secaoEditar"),
    path('secaoUsuario/listaObjetosEditar/<str:tipo>', listaObjetosEditar, name="listaObjetosEditar"),
    path('secaoUsuario/listaObjetosApagar/<str:tipo>', listaObjetosApagar, name="listaObjetosApagar"),
    path('secaoUsuario/listaObjetosApagarAutor/<str:tipo>', listaObjetosApagarAutor, name="listaObjetosApagarAutor"),
    path('secaoUsuario/secaoGenerica/<str:tipo>', secaoGenerica, name="secaoGenerica"),
    path('secaoUsuario/secaoGenerica02/<str:tipo>', secaoGenerica02, name="secaoGenerica02"),
    path('secaoUsuario/secaoGenericaVideo/<str:tipo>', secaoGenericaVideo, name="secaoGenericaVideo"),
    path('secaoUsuario/secaoGenericaVideo02/<str:tipo>', secaoGenericaVideo02, name="secaoGenericaVideo02"),
    path('secaoUsuario/secaoComfirmacao/<str:tipo>/<int:pk>', secaoApagar, name="secaoApagar")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
