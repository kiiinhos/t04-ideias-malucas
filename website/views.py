from django.shortcuts import render
from website.models import Pessoa
from website.models import Ideia


# Create your views here.

def index(request):
    # essa pagina vai cadastrar uma pessoa
    contexto={}
    
    if request.method =='POST':
       pessoa = Pessoa()
       pessoa.nome = request.POST.get('nome')
       pessoa.sobrenome = request.POST.get('sobrenome')
       pessoa.email = request.POST.get('email')
       pessoa.genero = request.POST.get('genero')
       pessoa.biografia = request.POST.get('biografia')
       pessoa.save()        
    
    return render(request,'index.html',contexto)

def sobre(request):
    #   essa pagina vai listar as ideias e seus criadores
    ideias= Ideia.objects.all()
    contexto = {'ideia':ideias}
    return render(request,'sobre.html',contexto)

def login(request):
    # essa pagina ira conferir se existe um usuario cadastrado
    # se sim retornara para pagina sobre
    # se não,retornará para pagina de cadastro com
    # uma mensagem "cadastre-se para criar uma ideia"
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa= Pessoa.objects.filter(email=email_form).first()

        if pessoa is None:
            # mandar para página de cadastro
            contexto = {'msg': 'Cdastre-se para criar uma ideia'}
            return render(request,'index.html',contexto)
        else:
            contexto= {'pessoa': pessoa}
            return render(request,'index.html',contexto)
     
     
    return render(request,'login.html',{})


def cadastrar_ideia(request):
    return render(request,'ideias.html')