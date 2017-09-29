from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# change index:
# which displays the latest 5 poll questions in the system, separated by commas, according to publication date:
from django.utils.datastructures import MultiValueDictKeyError

from .models import Question, Choice


def index(request):
    """
    1. 모든 Q를 출력하는 View구현
    context dict 객체 생성,
        'questions'키에
        모든 Question객체를 DB에서 가져온 QuerySet을 할당

    render함수를 사용해서 'polls/index.html'을
    context로 rendering 한 결과를 리턴

    2. 템플릿 파일들이 있는 디렉토리를 settings.py에 설정
        settings.py에 TEMPLATE_DIR를 지정
        TEMPLATE = ...설정의 'DIRS'키를 갖는 리스트에 TEMPLATE_DIR추가

    3. 템플릿 파일 생성, Question들을 출력
        polls/index.html파일을 생성
        해당 템플릿에 'questions'키로 전달된 QuerySet을 for loop하며
        각 loop에 해당하는 Question객체의 title 출력

    :param request:
    :return:
    """
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/question.html', {'question': question})


def results(request):
    pass


def vote(request, pk):
    """
    :param request:
    :param choice_pk:
    :return:
    """
    if request.method == 'POST':
        try:
            question = Question.objects.get(pk=pk)
            choice_pk = request.POST.get('choice_pk')
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
            question = choice.question
        except Question.DoesNotExist:
            return redirect('index')
        except MultiValueDictKeyError:
            pass
        except Choice.DoesNotExist:
            pass
        return redirect(question_detail, pk=question.pk)
    else:
        return HttpResponse("접근 권한이 없습니다", status=403)


def graphed_results(request, pk):
    """

    :param request:
    :param question_pk:
    :return:
    """

    return HttpResponse(Question.objects.get(pk=pk))
