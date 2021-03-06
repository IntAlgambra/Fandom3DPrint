from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Question, PrintingOrder, ModelingOrder
from .forms import CaptchaForm

def index(request):
    form = CaptchaForm()
    message_storage = messages.get_messages(request)
    return render(request, 'main/index.html', {'form': form, 'messages': message_storage})

def get_question(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message_text')
            if request.FILES:
                user_file = request.FILES['3d_file']
                q = Question(sender_name = name, sender_email = email, question_text = message, question_file = user_file)
            else:
                q = Question(sender_name = name, sender_email = email, question_text = message)
            try:
                q.full_clean()
                q.save()
                messages.success(request, 'Вопрос отправлен!')
            except:
                messages.error(request, 'Введенные данные некорректны!')

        # testing case with ignoring captcha
        elif request.POST.get('captcha_handler'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message_text')
            if request.FILES:
                user_file = request.FILES['3d_file']
                q = Question(sender_name = name, sender_email = email, question_text = message, question_file = user_file)
            else:
                q = Question(sender_name = name, sender_email = email, question_text = message)
            q.full_clean()
            q.save(using='testing')

        else:
            messages.error(request, 'Возникла ошибка, попробуйте еще раз.')

    return HttpResponseRedirect('/')

def get_printing_order(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            material = request.POST.get('material')
            quality = request.POST.get('quality')
            color = request.POST.get('color')
            order_file = request.FILES['3d_file']
            order = PrintingOrder(sender_name=name, sender_email=email, material=material, quality=quality, color=color, order_file=order_file)
            try:
                order.full_clean()
                order.save()
                messages.success(request, 'Заказ отправлен!')
            except:
                messages.error(request, 'Введенные данные некорректны!')
        #Testing case, ignoring captcha
        elif request.POST.get('captcha_handler'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            material = request.POST.get('material')
            quality = request.POST.get('quality')
            color = request.POST.get('color')
            order_file = request.FILES['3d_file']
            order = PrintingOrder(sender_name=name, sender_email=email, material=material, quality=quality, color=color, order_file=order_file)
            order.full_clean()
            order.save(using='testing')
        else:
            messages.error(request, 'Возникла ошибка, попробуйте еще раз')

    return HttpResponseRedirect('/')

def get_modeling_order(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            description = request.POST.get('model_description')
            order_file = request.FILES['3d_file']
            order = ModelingOrder(sender_name=name, sender_email=email, order_description=description, order_file=order_file)
            try:
                order.full_clean()
                order.save()
                messages.success(request, 'Заказ отправлен!')
            except:
                messages.error(request, 'Введенные данные некорректны!')
        #Testing case, ignoring captcha
        elif request.POST.get('captcha_handler'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            description = request.POST.get('model_description')
            order_file = request.FILES['3d_file']
            order = ModelingOrder(sender_name=name, sender_email=email, order_description=description, order_file=order_file)
            order.full_clean()
            order.save(using='testing')
        else:
            messages.error(request, 'Возникла ошибка, попробуйте еще раз.')

    return HttpResponseRedirect('/')


