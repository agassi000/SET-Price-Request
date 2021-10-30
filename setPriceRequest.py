from bs4 import BeautifulSoup
import requests

ticker = input("Please enter the ticker symbol --> ").strip()
html_text = requests.get('https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=' + ticker +'&ssoPageId=9&selectPage=1')

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

print('%s baht' % (value1 + value2 + value3).strip())
