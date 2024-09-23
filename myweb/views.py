from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from django.core.files.storage import FileSystemStorage
import uuid

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

# Post 방식의 form 데이터를 처리하는 함수
#@csrf_exempt
def formdata(request):
    # POST 방식으로 전달된 데이터를 추출
    # request.POST['key'] : key에 해당하는 데이터를 추출
    # request.POST.get('key') : key에 해당하는 데이터를 추출
    # request POST.get('key', 'default_value') : key에 해당하는 데이터가 없는 경우 default_value를 반환
    
    name = request.POST.get('name', 'no_name')
    nickname = request.POST.get('nickname', 'no_nickname')
    return HttpResponse("이름 : " + name + ", 별명 : " + nickname)

# Post 방식의 JSON 데이터를 처리하는 함수
#@csrf_exempt
def requestbody(request):
    # POST 방식으로 전달된 데이터를 추출
    # request.body : body에 해당하는 데이터를 추출
    # request.body.decode() : body에 해당하는 데이터를 추출
    
    # dict 형태로 리턴하기 위해서 json.loads() 함수를 사용
    user = json.loads(request.body)
    
    return HttpResponse("이름 : " + user['name'] + ", 별명 : " + user['nickname'])


def fileupload(request):
    # POST 방식으로 전달된 파일을 추출
    file = request.FILES['file']
    
    # 파일 저장 경로 설정
    fs = FileSystemStorage(location="media/itstudy", base_url="media/itstudy")
    
    # 원래 파일 이름을 추출
    originalname = file.name
    
    # UUID를 사용하여 고유한 파일 이름을 생성 (파일 확장자 유지)
    unique_filename = str(uuid.uuid1()) + "_" + originalname
    
    # 파일을 저장
    filename = fs.save(unique_filename, file)
    
    # 저장된 파일의 URL 생성
    upload_fileurl = fs.url(filename)
    
    return HttpResponse(f"변경된 파일 이름: {filename} 파일의 URL: {upload_fileurl}")
