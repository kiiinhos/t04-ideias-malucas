from django.shortcuts import render, redirect
from website.models import Pessoa
from website.models import Ideia
# Create your views here.

def index(request):
    # essa pagina é de cadastro
    contexto={}
    if request.method == 'POST':
        email_user = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_user)
        if pessoa is  None:
            contexto = {'msg':'Email já existe'}
        else:    
            pessoa = Pessoa()
            pessoa.nome = request.POST.get('nome')
            pessoa.sobrenome = request.POST.get('sobrenome')
            pessoa.email = request.POST.get('email')
            pessoa.senha = request.POST.get('senha')
            pessoa.genero = request.POST.get('genero')
            pessoa.biografia = request.POST.get('biografia')
            pessoa.save()
            return render(request,'login.html',{'msg':'Pode Logar'})

    return render(request, 'index.html',contexto)

def sobre(request):
    contexto={}
    if request.method == 'POST':
        categoria = request.POST.get('categorias')
        ideias = Ideia.objects.filter(categorias=categoria).all()
        contexto= {
            'ideias':ideias
        }
        if categoria == 'TODAS':
            ideias = Ideia.objects.all()
            contexto = {
            'ideias':ideias
            }

    return render(request, 'sobre.html', contexto)

def login(request):
    contexto = {}
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        pessoa_bd = Pessoa.objects.filter(email=email_form).first()
        if pessoa_bd is None:
            contexto = {'msg':'Cadastre-se aqui primeiro amg :)'}
            return render(request,'index.html',contexto)
        elif pessoa_bd.senha == senha_form:
            contexto = {'pessoa': pessoa_bd}
            return render(request,'ideias.html',contexto)
        else:
            contexto = {'msg':'Usuario ou senha invalidos'}

    return render(request, 'login.html',contexto)


def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categorias = request.POST.get('categorias')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save() 
            return redirect('/sobre') 
    return render(request,'ideias.html',{})
