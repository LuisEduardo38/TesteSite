from django.db import models

class Genero(models.Model):
    descricao = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return f"Gênero: {self.descricao}"

class Observacoes(models.Model):
    descricao = models.CharField(max_length=30,  blank=False)
    
    def __str__(self):
        return f"Observacão: {self.descricao}"

class Video(models.Model):
    tituloVideo = models.CharField(max_length=50, blank=True)
    urlVideo = models.URLField()
    
    def pegaEmbarcaURL(self):
        videoId = self.urlVideo.split("/")[-1]
        return f"https://www.youtube.com/embed/{videoId}"
    
    def __str__(self):
        return f"Título: { self.tituloVideo }"

class Autor(models.Model):
    imagem = models.ImageField(upload_to="media", blank=True)
    nome = models.CharField(max_length=80, blank=False)
    naturalidade = models.CharField(max_length=100, blank=False)
    nascimento = models.DateField(blank=False)
    generoAutor = models.ManyToManyField(Genero)
    publicoAlvo = models.CharField(max_length=50, blank=False)
    editora = models.CharField(max_length=70, blank=True)
    resumo = models.TextField(blank=False)
    capaMaisLido01 = models.ImageField(upload_to="media", blank=True)
    capaMaisLido02 = models.ImageField(upload_to="media", blank=True)
    capaMaisLido03 = models.ImageField(upload_to="media", blank=True)
    maisLido = models.TextField(blank=True)
    livros = models.TextField(blank=True)
    
    def __str__(self):
        return f"Autor(a): {self.nome} - {self.editora}"
    
class Livro(models.Model):
    capa = models.ImageField(upload_to="media", blank=True)
    titulo = models.CharField(max_length=80, blank=False)
    autor = models.ForeignKey(Autor, on_delete= models.PROTECT)
    generoLivro = models.ManyToManyField(Genero, blank=False)
    lancamento = models.DateField(blank=False)
    nota = models.IntegerField(blank=False)
    observacao = models.ManyToManyField(Observacoes, blank=False)
    resumo = models.TextField(blank=True)
    introducao = models.TextField(blank=False)
    desenvolvimento = models.TextField(blank=False)
    conclusao = models.TextField(blank=False)
    imagem01 = models.ImageField(upload_to="media", blank=True)
    imagem02 = models.ImageField(upload_to="media", blank=True)
    videos = models.ManyToManyField(Video, blank=True)
    
    def __str__(self):
        return f"Livro: {self.titulo} - {self.autor}"