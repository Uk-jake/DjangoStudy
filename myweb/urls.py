from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("get/", views.showGetDescription),
    path("get/<str:itemid>", views.getItem),
    
    # GET 방식의 queryString을 처리하는 함수
    path('querystring', views.queryString),
    
    # Post 방식의 form 데이터를 처리하는 함수
    path('formdata',views.formdata),
    
    # Post 방식의 JSON 데이터를 처리하는 함수
    path('requestbody', views.requestbody),
    
    # 파일 업로드를 처리하는 함수
    path('fileupload', views.fileupload),
]
 