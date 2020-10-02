from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def dbSave(initialUrl, urls_internas):
#Criando entrada na tabela da url inicial
    link_inicial = url_inicial()
    link_inicial.link = initialUrl
    link_inicial.save()

#Criando as entradas relacionadas a url inicial
    for url in urls_internas:
        url_relacionadas = urls_relacionadas()
#Fazendo a relação entre as tabelas
        url_relacionadas.id_url_inicial = url_inicial.objects.get(pk = link_inicial.id_url_inicial)
        url_relacionadas.link = url
        url_relacionadas.save()

    resultado = list(urls_relacionadas.objects.filter(id_url_inicial = link_inicial.id_url_inicial).values())

    return resultado

def url_getter(request):
    #coletando a url enviada na request
    initialUrl = request.body.decode("utf-8")
    #inicialização de lista única
    urls_list = set()
    #crawler para pegar as urls de forma recursiva, limitadas a 2 buscas para evitar problemas de performance
    x = crawl(initialUrl, 2, urls_list)
    #ao final do crawler, função para gravar no banco de dados as urls
    y = dbSave(initialUrl, urls_list)
    
    return JsonResponse({'resultado':y})