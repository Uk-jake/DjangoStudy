from django.shortcuts import render

from django.http import HttpResponse

# index 함수 정의
def index(request):
    # 직접 태그를 생성해서 출력
    return HttpResponse("Hello, Django!")


def htmlpage(request):
    return render(request, 'index.html', {'message': 'this is a message from views.py'})

def test(request):
    return HttpResponse("This is a test page.")

def showGetDescription(request):
    return render(request, 'show.html', {'message': 'this is a description page'})

def getItem(request, itemid):
    return HttpResponse(f"Item ID: {itemid}")

# GET 방식의 queryString을 처리하는 함수
def queryString(request):
    # GET 방식으로 전달된 데이터를 추출
    # request.GET['key'] : key에 해당하는 데이터를 추출
    # request.GET.get('key') : key  에 해당하는 데이터를 추출
    # request.GET.get('key', 'default_value') : key에 해당하는 데이터가 없는 경우 default_value를 반환
    
    # 아래와 같이 key가 없는 경우 에러 발생
    # return HttpResponse(request.GET['name'])
    
    # key가 없는 경우 default_value 반환
    return HttpResponse(request.GET.get('name', 'no_name'))
    