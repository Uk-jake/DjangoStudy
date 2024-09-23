from django.shortcuts import render

from django.http import HttpResponse

# index 함수 정의
def index(request):
    # 직접 태그를 생성해서 출력
    return HttpResponse("Hello, Django!")


def htmlpage(request):
    return render(request, 'index.html', {'message': 'Hello, Django!'})

def test(request):
    return HttpResponse("This is a test page.")