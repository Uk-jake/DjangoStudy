from django.urls import path

from . import views

urlpatterns = [
    # /myweb의 index 페이지를 호출하는 URL
    path("item", views.showItems),
    
    # itemid를 파라미터로 받아서 출력하는 URL
    path("item/<int:itemid>", views.showItemDetail),
    
    # item을 정보를 받아 DB에 저장하는 URL
    path("item/add", views.addItem),
    
    # item 정보를 수정하는 URL
    path("item/update/<int:itemid>", views.updateItem),
    
    # item 정보를 삭제하는 URL
    path("item/delete/<int:itemid>", views.deleteItem),
    
    path("get", views.showGetDescription),
    #path("get/<str:itemid>", views.getItem),
    
    # GET 방식의 queryString을 처리하는 함수
    path('querystring', views.queryString),
    
    # Post 방식의 form 데이터를 처리하는 함수
    path('formdata',views.formdata),
    
    # Post 방식의 JSON 데이터를 처리하는 함수
    path('requestbody', views.requestbody),
    
    # 파일 업로드를 처리하는 함수
    path('fileupload', views.fileupload),
    
    # Cookie를 만드는 함수
    path('setcookie', views.setcookie),
    
    # Cookie를 읽는 함수
    path('getcookie', views.getcookie)
]
 