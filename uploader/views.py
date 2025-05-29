from django.shortcuts import render
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        # Aqui você pode processar o arquivo enviado, por enquanto só retorna um texto
        return HttpResponse("Arquivo recebido!")
    return render(request, 'upload.html')  # Um template básico para mostrar o formulário
