from django.shortcuts import render
from django.core.paginator import Paginator



global_info = {
    "tags": [
        f"this_is_{j}_tag"
        for j in range(10)
        ],
    "best_memb": [
        f"angelname{k}"
        for k in range(10)]
}

questions = [
    {
        "id": f'{i}',
        "avatar": f"/static/img/avatar{i}.png",
        "title": f"title {i}", 
        "text": f"this is text for {i} question", 
        "best_ans": f"this is best answer for {i} question", 
        "numb_of_answers": f"{i+1}",
        "tags": global_info['tags'][:3],
        "like_counter": f"{i}",
        "dislike_counter": f"{i}",
    } for i in range(30)
]

answers = [
    {
        "number": {i},
        "avatar": f"/static/img/avatar{i}.png",
        "text": f"this is text for {i} answer", 
        "like_counter": f"{i}",
        "dislike_counter": f"{i}",
        "correct_or_no": True,
    } for i in range(1, 7)
]

def paginate(objects_list, request):
    per_page = request.GET.get('limit', 6)
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return content


def index(request):
    return render(request, "index.html", {'contentlist': paginate(questions,request), 'global_info' : global_info})

def hot(request):
    return render(request, "hot.html", {'contentlist': paginate(questions,request), 'global_info' : global_info})

def login(request):
    return render(request, "login.html", {'global_info' : global_info})

def signup(request):
    return render(request, "signup.html", {'global_info' : global_info})

def ask(request):
    return render(request, "ask.html", {'global_info' : global_info})

def new(request):
    return render(request, "index.html", {'global_info' : global_info})

def tag(request, tagid):
    return render(request, "tag.html", {'contentlist': paginate(questions,request), 'tagid': tagid, 'global_info' : global_info})

def question(request, id):
    return render(request, "question.html", {'question': questions[id], 'contentlist': paginate(answers,request), 'id': id, 'global_info' : global_info})