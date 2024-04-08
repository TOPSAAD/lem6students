from django.shortcuts import get_object_or_404, render, redirect
from django.http import FileResponse, Http404
from django.views.decorators.http import require_POST
from .models import Cours,Exercice,DS,Probleme,DL, Eleve  ,Contact
# Create your views here.
logged = False

def login(request):
    global logged
    session = request.session
    USERS = Eleve.objects.all()
    if(session['logged'] == True):
        return redirect(index)
    x = {}
    x['correct'] = True
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        for user in USERS:
            if username == user.username and password == user.password:
                logged = True
                session['logged'] = True
                return redirect(index)
        if(session['logged'] == False):
            x['correct'] = False
        
    
    return render(request, 'pages/login.html',x)

def index(request):
    session = request.session
    # del session['logged']
    global logged
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    x={
        'cours':Cours.objects.all()[:4]
    }
    
    return render(request, 'pages/index.html',x)


def pages(request, id, cte, sub):
    session = request.session
    # del session['logged']
    global logged
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    # product = get_object_or_404(Product, id=id)
    
    x={
        'id':id,
        'cte':cte,
        'sub':sub,
        'categories':['Logique et algèbre','Analyse','Algèbre et arithmétique']
    }
    if(sub == 'cours'):
        x['all'] = Cours.objects.filter(classe = id , matiere = cte)
    elif(sub == 'exos'):
        x['all'] = Exercice.objects.filter(classe = id , matiere = cte)
        
    elif(sub == 'ds'):
        x['all'] = DS.objects.filter(classe = id , matiere = cte)
    elif(sub == 'prob'):
        x['all'] = DS.objects.filter(classe = id , matiere = cte)
    elif(sub == 'ds'):
        x['all'] = DS.objects.filter(classe = id , matiere = cte)
    elif(sub == 'dmdl'):
        x['all'] = DL.objects.filter(classe = id , matiere = cte)
    return render(request, 'pages/cours.html', x)

def cours_details(request,id,sub):
    session = request.session
    # del session['logged']
    global logged
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    x = {
        
    }
    if(sub == 'cours'):
        x['c'] = get_object_or_404(Cours, id=id)
    elif(sub == 'exos'):
        x['c'] = get_object_or_404(Exercice, id=id)
    elif(sub == 'ds'):
        x['c'] = get_object_or_404(DS, id=id)
    elif(sub == 'prob'):
        x['c'] = get_object_or_404(Probleme, id=id)
    elif(sub == 'dmdl'):
        x['c'] = get_object_or_404(DL, id=id)
    return render(request, 'pages/cours_details.html', x)

# def pdf_view(request,file):
#     try:
#         return FileResponse(open('/media/CamScanner_27-02-2024_16.46_2.pdf', 'rb'), content_type='application/pdf')
#     except FileNotFoundError:
#         raise Http404()

def contact(request):
    session = request.session
    # del session['logged']
    global logged
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    sender = Contact()
    if(request.method == 'POST'):
        sender.nom = request.POST['nom']
        sender.email = request.POST['email']
        sender.message = request.POST['message']
        sender.save()
        
        
    return render(request, 'pages/contact.html')