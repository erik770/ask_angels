from django.shortcuts import render
from django.core.paginator import Paginator

from app.models import Answer, ProfileManager, Question, TagManager



global_info = {
    "tags": TagManager.best()[:10],
    "best_memb": ProfileManager.best()[:10]
}


def paginate(objects_list, request):
    per_page = request.GET.get('limit', 6)
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return content


def index(request):
    questions = Question.objects.get_new_questions()
    return render(request, "index.html", {'contentlist': paginate(questions,request), 'global_info' : global_info})

def hot(request):
    questions = Question.objects.get_hot_questions()
    return render(request, "hot.html", {'contentlist': paginate(questions,request), 'global_info' : global_info})

def login(request):
    return render(request, "login.html", {'global_info' : global_info})

def signup(request):
    return render(request, "signup.html", {'global_info' : global_info})

def ask(request):
    return render(request, "ask.html", {'global_info' : global_info})

def new(request):
    questions = Question.objects.get_new_questions()
    return render(request, "index.html", {'contentlist': paginate(questions,request), 'global_info' : global_info})

def tag(request, tagid):
    questions = Question.objects.get_questions_by_tag(tagid)
    return render(request, "tag.html", {'contentlist': paginate(questions,request), 'tagid': tagid, 'global_info' : global_info})

def question(request, id):
    question = Question.objects.get(pk=id)
    answers = Answer.objects.get_by_question(question)
    return render(request, "question.html", {'question': question, 'contentlist': paginate(answers,request), 'id': id, 'global_info' : global_info})