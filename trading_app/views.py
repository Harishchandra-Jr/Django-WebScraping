from django.shortcuts import render
from trading_app.models import todays

# Create your views here.


def index(request):
    return render(request,'trading_app/index.html')

def trading(request):
    trading_data = todays.objects.order_by('company_name')
    data_dict = {'access_data':trading_data}
    return render(request,'trading_app/trading.html', context =data_dict )

def base(request):
    return render(request,'trading_app/base.html')