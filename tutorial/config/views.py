import re

from django.conf import settings
import os

from django.http import HttpResponseNotFound, FileResponse, HttpResponse


def static_file(request):
    """
    request.path에서
        /static/<FILE_PATH>/
    filepath변수에 FILE_PATH에 해당하는 문자열을 변수로 할당

    os.path모듈을 사용해 settings.BASE_DIR로부터
    현재 프로젝트 구조의 static폴더내부에서 filepath에 해당하는 파일이 있는지 검사
    있으현 파일 리턴 없으면 404 리턴

    :param request:
    :return:
    """
    filepath = re.match(r'/static/(.*)', request.path)[0]
    # return HttpResponse(filepath)
    #os.path모듈을 사용해 settings.BASE_DIR로부터
    #현재 프로젝트 구조의 static폴더내부에서 filepath에 해당하는 파일이 있는지 검사
    file = settings.BASE_DIR + filepath
    mime_type = mime.guess_type(file)

    if os.path.exists(file):
        return FileResponse(open(file, 'rb'),content_type=mime_type)
    else:
        return HttpResponseNotFound('File Not Found')
