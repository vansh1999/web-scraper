import requests
import pandas
from bs4 import BeautifulSoup

def stockPrice():

    page = requests.get('https://in.finance.yahoo.com/quote/TSLA?p=TSLA')
    soup = BeautifulSoup(page.content , 'lxml')

    content = soup.find_all('div' , {'class' : 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'})[0]

    table = content.find_all('table' , {'class' : 'W(100%)'})[0]



    close = table.find_all('td' , {'class' : 'Ta(end) Fw(600) Lh(14px)'})[0]
    opent = table.find_all('td' , {'class' : 'Ta(end) Fw(600) Lh(14px)'})[1]


    current_close = close.find(class_ = 'Trsdu(0.3s)').get_text()
    current_open = opent.find(class_ = 'Trsdu(0.3s)').get_text()

    return current_close , current_open

    # print('current close : ' + current_close)
    # print('current open : ' + current_open)

while True:
    print("current close and open " + str(stockPrice()))











