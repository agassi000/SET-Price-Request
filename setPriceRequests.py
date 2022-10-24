from bs4 import BeautifulSoup
from tkinter import *
import requests, webbrowser

ws = Tk()
ws.title("Ticker Lookup")
ws.geometry('500x500')
ws['bg'] = '#ff10f0'

tiksym = Entry(ws)
tiksym.pack(pady=30)


def scrapedData():
    ticker = tiksym.get()
    html_text = requests.get('https://classic.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=' + ticker +'&ssoPageId=9&selectPage=1')

    soup = BeautifulSoup(html_text.content, 'html.parser')

    StockLatestPriceRed = soup.find('div', class_='col-xs-6 col-xs-offset-6 colorRed')
    StockLatestPriceUnch = soup.find('div', class_='col-xs-6 col-xs-offset-6')
    StockLatestPriceGreen = soup.find('div', class_='col-xs-6 col-xs-offset-6 colorGreen')

    if StockLatestPriceRed is not None:
      value1 = StockLatestPriceRed.text.strip()
    else:
      value1 = ''

    if StockLatestPriceGreen is not None:
      value2 = StockLatestPriceGreen.text.strip()
    else:
      value2 = ''

    if StockLatestPriceUnch is not None:
      value3 = StockLatestPriceUnch.text.strip()
    else:
      value3 = ''

    if value1 + value2 + value3 == '':
      Label(ws, text="There is no "+ ticker.upper() + " in the SET (The Stock Exchange of Thailand)", pady=5, bg='#ff10f0').pack()
    else:
      web = 'https://classic.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=' + ticker + '&ssoPageId=9&selectPage=1'
      Label(ws, text=ticker.upper() + " is "+'%s baht' % (value1 + value2 + value3), pady=5, bg='#ff10f0').pack()
      link = Label(ws, text="Check it? Click here!", fg="blue", cursor="hand2")
      link.pack()
      link.bind("<Button-1>", lambda e:
      callback(web))

    def callback(url):
      webbrowser.open_new_tab(url)

Button(
    ws,
    text="Lookup!!!",
    padx=10,
    pady=5,
    command=scrapedData
    ).pack()

ws.mainloop()
