from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# change index:
# which displays the latest 5 poll questions in the system, separated by commas, according to publication date:
from polls.models import Question


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
    context= {
        'questions': questions
    }

    return render(request, 'polls/index.html', context)

def detail(request):
    pass

def results(request):
    pass

def vote_action(request):
    pass
