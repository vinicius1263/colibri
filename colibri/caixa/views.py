from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Mesa, Produto, Produtolancado


# Create your views here.
def listamesa(request):
    mesa = Mesa.objects.all()
    return render(request, 'caixa/listamesa.html', {'mesa': mesa})


@csrf_exempt
def lancar(request):
    dados = request.POST
    mesa = Mesa.objects.filter(numero=dados['numMesa']).first()
    if mesa is None:
        mesa = Mesa(numero=dados['numMesa'])
        mesa.save()
    produto = Produto.objects.filter(cod=dados['CodProduto']).first()
    if produto is None:
        return HttpResponse('produto nao cadastrado')
    produtolancado = Produtolancado(
        cod=produto.cod, nome=produto.nome, preco=produto.preco, mesa=mesa
    )
    produtolancado.save()
    return HttpResponse('ok')


def fechar(request):
    return render(request, 'caixa/fechar.html')


def lancando(request):
    return render(request, 'caixa/lancando.html')


def tranferir(request):
    return render(request, 'caixa/transferir.html')

@csrf_exempt
def exibir(request):
    dados = request.POST
    mesa = Mesa.objects.filter(numero=dados['numero']).first()
    if mesa is None:
        return HttpResponse('a mesa nao esta aberta')
    else:
        produtoslancados = Produtolancado.objects.filter(mesa=mesa).first()
    return render(request, 'caixa/exibir.html', {'mesa': mesa, 'produtoslancados': produtoslancados})


def testes(request):
    return render(request, 'caixa/testes.html')