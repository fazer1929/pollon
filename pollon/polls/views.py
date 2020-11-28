from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect,JsonResponse
from django.urls import reverse

# Create your views here.
from .models import Question , Choice

#Get Quesitons
def index(request):
    latest_question = Question.objects.order_by('-pub_date').filter(open_for_all=True)
    return render(request,"polls/index.html",{
        'latest_question' : latest_question
    })

def details(request,question_id):
    try:
        question = Question.objects.get(pk=int(question_id))
    except Question.DoesNotExist:
        raise Http404("Question Dies Not Exist")
    return render(request,"polls/details.html",{
        'question':question
    })

def results(request,question_id):
    question =  get_object_or_404(Question,pk=int(question_id))
    return render(request,'polls/results.html',{
        'question':question
    })

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,"polls/details.html",{
            'question':question,
            "error":"You Didn't Select A Choice",
        
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

def resultsData(request,question_id):
    votes=[]
    question = Question.objects.get(pk=int(question_id))
    choices = question.choice_set.all()
    for i in choices:
        votes.append({
            i.choice_text:i.votes
        })
    return JsonResponse(votes,safe=False)
