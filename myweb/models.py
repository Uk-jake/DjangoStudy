# Create your models here.
# 데이터베이스에서 사용할 테이블과 클래스를 매핑하는 파일
from django.db import models
from enum import unique


# 소유자 정보를 저장하는 테이블
class Owner(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=128)

# 자동차 브랜드 정보를 저장하는 테이블
class Brand(models.Model):
    brand_name = models.CharField(max_length=128, unique=True)

# 자동차 모델 정보를 저장하는 테이블
class Car_Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=128)

# 자동차 정보를 저장하는 테이블
class Car(models.Model):
    car_number = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, on_delete=models.CASCADE)

# 상품 정보를 저장하는 테이블
class Item(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    pictureurl = models.CharField(max_length=20)

