from django.shortcuts import render

def home(request):
    if request.method == "GET":
        return render (request, 'index.html')
    
    elif request.method == "POST":
        capital = float(request.POST.get('capital_investimento', 0))
        porcent = float(request.POST.get('taxa_de_porcentagem', 0))
        years = float(request.POST.get('taxa_a_a', 0 ))

        taxa_de_juros = porcent / 100
        result = (capital * (1 + taxa_de_juros ) ** years)
        print(result)


        return render (request, 'index.html', {'resultado': f'{result:.2f}'})

