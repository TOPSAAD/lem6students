from django.shortcuts import get_object_or_404, render, redirect
from django.http import FileResponse, Http404
from django.views.decorators.http import require_POST
from .models import Cours,Exercice,Probleme,CNC, Eleve  ,Contact
# Create your views here.


def login(request):
    
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
                session['id'] = user.id
                session['username'] = username
                session['pdp'] = user.image1.url
                session['nom'] = user.nom
                session['prenom'] = user.prenom
                session['email'] = user.email
                session['phone'] = user.telephone
                session['birth'] = str(user.anniv)
                

                return redirect(index)
        if(session['logged'] == False):
            x['correct'] = False
        
    
    return render(request, 'pages/login.html',x)

def index(request):
    session = request.session
    # del session['logged']
    
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        
    
    x={
        'cours':Cours.objects.all()[:4],
        'logged':session['logged'],
    }
    
    return render(request, 'pages/index.html',x)

def account(request):
    session = request.session
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)

    x = {
        'logged':session['logged'],
        'username':session['username'],
        'usersexists':False,
        'pdp':session['pdp'],
        'nom':session['nom'],
        'prenom':session['prenom'],
        'email':session['email'],
        'phone':session['phone'],
        'birth':session['birth'],

    }
    if(request.method == 'POST'):
        if('image' in request.POST):
            
            image = request.FILES['image']
            
            U = Eleve.objects.get(id = session['id'])
            U.image1 = image
            U.save()
            session['pdp'] = U.image1.url
            # print(session['pdp'])
        else:
            username = request.POST['username']
            prenom = request.POST['prenom']
            nom = request.POST['nom']
            email = request.POST['email']
            phone = request.POST['phone']
            birth = request.POST['birth']
            P = Eleve.objects.filter(username = username)
            if(len(P)>1):
                x['usersexists'] = True
            elif((len(P)==1 and P[0].id == session['id']) or len(P)==0):
                x['usersexists'] = False
                U = Eleve.objects.get(id = session['id'])
                # U.update(username=username , prenom = prenom , nom = nom , email = email , telephone = phone , anniv = birth)
                U.username = username
                U.prenom = prenom
                U.nom = nom
                
                U.email = email
                U.phone = phone
                U.anniv = birth
                U.save()
                session['username'] = username
                session['nom'] = nom
                session['prenom'] = prenom
                session['email'] = email
                session['phone'] = phone
                session['birth'] = birth
        x = {
                    'logged':session['logged'],
                    'username':session['username'],
                    'usersexists':False,
                    'pdp':session['pdp'],
                    'nom':session['nom'],
                    'prenom':session['prenom'],
                    'email':session['email'],
                    'phone':session['phone'],
                    'birth':session['birth'],

                }
            # print(session['prenom'])
            

    
    
    return render(request, 'pages/account.html',x)


def pages(request, id, cte, sub):
    session = request.session
    # del session['logged']
    
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    # product = get_object_or_404(Product, id=id)
    
    x={
        'id':id,
        'cte':cte,
        'sub':sub,
        'logged':session['logged'],
        'categories':['Logique et algèbre','Analyse','Algèbre et arithmétique']
    }
    if(sub == 'cours'):
        x['all'] = Cours.objects.filter(classe = id , matiere = cte)
    elif(sub == 'exos'):
        x['all'] = Exercice.objects.filter(classe = id , matiere = cte)
        
    elif(sub == 'prob'):
        x['all'] = Probleme.objects.filter(classe = id , matiere = cte)
    elif(sub == 'cnc'):
        x['all'] = CNC.objects.filter(classe = id , matiere = cte)
    
    return render(request, 'pages/cours.html', x)

def cours_details(request,id,sub):
    session = request.session
    # del session['logged']
    
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    x = {
        'logged':session['logged'],
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
   
    if('logged' not in session or session['logged'] == False):
        session['logged'] = False
        return redirect(login)
    
    sender = Contact()
    if(request.method == 'POST'):
        sender.nom = request.POST['nom']
        sender.email = request.POST['email']
        sender.message = request.POST['message']
        sender.save()
        
    x = {
        'logged':session['logged'],
    }
    return render(request, 'pages/contact.html',x)