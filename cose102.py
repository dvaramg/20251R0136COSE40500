# -*- coding: utf-8 -*-
"""COSE102_2022Fall_04_신준송.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DshijXMjgxIwgiu78aTDcY3eVrKIl9lo
"""

print('돈을 두 배로 불려 드립니다!')
bank=input('현재 가지 금액 입력:')
bank=int(bank)
print(bank*2,'로 돌려드렸습니다!')

10*3

print('돈을 두 배로 불려 드립니다!')
bank=int(input('현재 가지 금액 입력:'))
bank=int(bank)
print(bank*2,'로 돌려드렸습니다!')

score=input()
score=int(score)

if(score>=70):
  print('합격')
else:
    print('다시보세요')

area=input()
area=int(area)

area=area*3.3

if(area<=49):
  print('청년')
if(area>49)and(area<=69):
  print('신혼부부')
if(area>69)and(area<=89):
  print('일반가구')
if(area>89):
  print('노년층')

area=input()
area=int(area)

area=area*3.3

if(area<=49):
  print('청년')
elif(area<=69):
  print('신혼부부')
elif(area<=89):
  print('일반가구')
else:
  print('노년층')



print('적중률 100% 김리 테스트를 시작합니다.')
print('당신은 중국음식점에 갔습니다.')
food=input('메뉴판에서 가장 먼저 보이는 것은?')
print()
print('분석 중..')
print()
print('당신은..')
print(food)
print('을 좋아하는 타임입니다.')

product=['T-shirt','Watches','Pants','Socks']

print(product[2])

product[3]='1+1 Socks'

print(product)

num_list=range(1,100)

num_list[98]

product=['T-shirt','Watches','Pants','Socks']

product[1]='50% discounts Watches'

print(product[1])

num_list=range(0,99,2)

len(num_list)

i=1

while(i<10):
  print('Muyaho~')
  print('그만크큼',i,'번 신나신 거지')
  i=1+1

i=1
total=0
print('Python 만보기')

while(i<=10):
  print('오늘',i,'보 걸었어요.')
  total=total+i
  i=i+1

print('지금까지 총',total,'보 걸었네요!')

print('Python 만보기')

for i in range(1,11):
  print('오늘',i,'보 걸었어요.')
  total=total+1

print('지금까지 총',total,'보 걸었네요!')

num=input()
num=int(num)

for i in range(2,num):
  if(num%2)==0:
    print('소수가 아닙니다')
    break
  else:
    print('소수입니다.')

for i in range(0,10):
  print(i)
  if(i>=10):
    print('BREAK')
    break
else:
  print('NO BREAK')

coffee=['americano','latte','mocha']

for menu in coffee:
  print(menu,'한 잔 할래요~')

num_list=range(100)

num_list[0]

product=['T-sirt','Watches','Pants','Socks']

print(product)

def func1():
  num1=50
  print(num2)

def func2():
   num2=70
   print(num2)
   func1()

num2=30

func2()

def fact_func(n):
  if(n==1):
    return 1
  else:
    return n*fact_func(n-1)

fact_func(5)

def fibo_func(n):
  if(n==1)or(n==2):
    return 1
  else:
    return fibo_func(n-1)+fibo_func(n-2)

#fibo_func(7)
fibo_func(4)

def list_nulti(input_list):
  result=1
  for i in input_list:
    result=result*i
  return result

list1=[input()]
list2=[input()]


if (list1==list2):
  print('yes')
else:
  print('no')

class Candidate:

  region='서울 성북 병'

  def _int_(self, name, gender, age, number, rating):
    self.name = name
    self.gender = gender
    self.age = age
    self.number = number
    self.rating = rating

import requests

url = 'https://www.genie.co.kr/chart/top200'
header_info = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}

page = requests.get(url, headers = header_info)
page=page.text

soup = BeautifulSoup(page, 'html.parser')

top50_songs_list = list()

for each_data in top50_songs :
  song_name = each_data.text
  song_name = song_name.strip()
  top50_songs_list.append(song_name)

print(top50_songs_list)
print(len(top50_songs_list))

!pip install selenium
!apt-get update
!apt install chromium-chreomediriver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

sepcific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver',options = specific_options)

driver.get('https:portal.korea.ac.kr/front/Intro.kpd')
time.sleep(1)
driver.save_screenshot('BEFORE.png')