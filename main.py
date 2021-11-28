#-----------------------------------------------위 API 는 공공데이터포털에 의하여 제공받았습니다. 위 API의 업데이트 주기는 보통 오전 10 시 이므로 새벽에는 작동하지 않을 수 있습니다-----------------------------------------------
import requests
from bs4 import BeautifulSoup
from time import strftime
from tkinter import *


todayDate = strftime("%Y%m%d");
# 현재날짜 20000101 형식으로 불러오기

#todayDate = '20210820'

open_api_key = 'PcSyYRiO9daLedfPzryTETfMiNaUAh4vR0K19F%2FbW6dNYLseO0f0Th7f1n2vC0Qv%2Bl3ggOwmgvQNyu6HHMoGMA%3D%3D'
# 공공데이터포털의 encode 키 값
params = '&pageNo=1&numOfRows=10&startCreateDt=' + todayDate + '&endCreateDt=' + todayDate
# 파라미터 값 분리
open_url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=' + open_api_key + params
# API URL 파라미터와 합치기


def getCoronaCnt():
    res = requests.get(open_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    # XML 도 html.parser 사용해서 파싱

    items = soup.find_all('item')
    # 모든 아이템을 items 변수처리
    realItem = items[18]
    # 18번째 아이템이 합계 데이터 이므로 변수처리
    # print(realItem)

    result = realItem.find('incdec').text
    # 결과 값(증가한 확진자 수) 는 item의 incdec 테그의 텍스트
    print(result)

    return result

getCoronaCnt()
coronaCnt = int(getCoronaCnt())



root = Tk()
root.title("Corona Clock") # GUI 제목
root.geometry("1024x600") # 1024x600 고정해상도 설정
root.resizable(False, False) # 창크키 조절 비허용
#root.attributes('-fullscreen', True)


def changeBackgroundColor():
    if coronaCnt > 3000 :
        root.configure(bg='#DB1F48')
        lbl1.config(bg='#DB1F48')
        lbl2.config(bg='#DB1F48')
        lbl3.config(bg='#DB1F48')
    elif coronaCnt > 3000 :
        lbl1.config(bg='#D67BA8')
        lbl2.config(bg='#D67BA8')
        lbl3.config(bg='#D67BA8')
        root.configure(bg='#D67BA8')
    elif coronaCnt > 3000 :
        lbl1.config(bg='#FFFF00')
        lbl2.config(bg='#FFFF00')
        lbl3.config(bg='#FFFF00')
        root.configure(bg='#FFFF00')
    elif coronaCnt < 3000 :
        lbl1.config(bg='#22CAE0')
        lbl2.config(bg='#22CAE0')
        lbl3.config(bg='#22CAE0')
        root.configure(bg='#22CAE0')

def time():
    nowTime = strftime("%H:%M:%S %p")
    minSecTime = strftime("%M%S")
    if minSecTime == '0000':
        print("새로고침 완료")
        getCoronaCnt()
        changeBackgroundColor()
    lbl1.config(text=nowTime)
    lbl1.after(1000, time)


lbl1 = Label(root, font=('calibri', 150, 'bold'),
            foreground='Black')
lbl1.pack(anchor='center')

lbl2 = Label(root, font=('calibri', 100, 'bold'),
            foreground='Black')
lbl2.pack(anchor='center')
lbl2.config(text="확진자수")

lbl3 = Label(root, font=('calibri', 190, 'bold'),
            foreground='Black')
lbl3.pack(anchor='center')
lbl3.config(text=getCoronaCnt())







changeBackgroundColor()
time()











mainloop() #창이 꺼지지 않게 메인루프



