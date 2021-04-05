from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from prices.models import PricesCard, PricesTable
from telebot.sendmessage import send_telegram_message

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PricesCard.objects.get(pk=1)
    pc_2 = PricesCard.objects.get(pk=2)
    pc_3 = PricesCard.objects.get(pk=3)
    prices_table = PricesTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'prices_table': prices_table,
                'form': form
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram_message(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {
            'name': name,
            'phone': phone
        })
    else:
        return render(request, './thanks.html')
