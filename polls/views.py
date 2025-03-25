from django.http import HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    latest_question_list = models.Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    # try:
    #     question = models.Question.objects.get(pk=question_id)
    # except models.Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)



def vote(requets, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
