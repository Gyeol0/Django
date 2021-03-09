from django.shortcuts import render
import requests
import random

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def DTL(request):
    foods = ['라면', '짜장면']
    numbers = [10, 20, 30, 40, 50]
    user_info ={
        'name': 'Gyeol',
        'location': 'seoul',
    }

    context = {
        'foods': foods,
        'user_info': user_info,
        'numbers': numbers,
    }
    return render(request, 'pages/DTL.html', context)

def question(request):
    return render(request, 'pages/question.html')

def answer(request):
    url = 'https://yesno.wtf/api'
    res = requests.get(url)
    ques = request.GET.get('ques')
    ans = res.json()
    print(ans)
    context = {
        'ans': ans.get('answer'),
        'img': ans.get('image'),
        'ques': ques,
    }
    return render(request, 'pages/answer.html', context)

def lotto(request):
    times = random.randint(1, 500)
    number = sorted(random.sample(range(1, 46), 6))
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={times}'
    res = requests.get(url)
    lotto_info = res.json()
    lotto_numbers = []
    answer = []
    count = 0
    for i in range(1, 7):
        lotto_num = lotto_info.get(f'drwtNo{i}')
        lotto_numbers.append(lotto_num)
        if lotto_num in number:
            answer.append(lotto_num)
            count += 1
    lotto_numbers.sort()
    context = {
        'times': times,
        'number': number,
        'answer': answer,
        'count': count,
        'lotto_numbers': lotto_numbers,
    }
    return render(request, 'pages/lotto.html', context)

def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'pages/dinner.html', context)
