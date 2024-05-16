from django.shortcuts import render



def index(request):
    context={'answer':''}
    if request.method == 'POST':
        input=request.POST['input']
        context={
            'length':len(input)
        }
    return render(request,"index.html",context)




def home(request):
    context={'answer':''}
    if request.method == 'POST':
        input=request.POST['input']
        promise=input.split()
        

        context={
                'promise':len(promise)
            }
    return render(request,"home.html",context)