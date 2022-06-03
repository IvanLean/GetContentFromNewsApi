import sre_constants
import requests
from googletrans import Translator
import googletrans
from bs4 import BeautifulSoup
from datetime import date

def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')

    return article.text



url = 'https://www.forbes.com/sites/billybambrough/2022/02/18/crypto-crash-bitcoin-now-braced-for-a-100-trillion-bombshell-that-could-boost-the-price-of-ethereum-bnb-solana-cardano-and-xrp/'
firstpart = "https://newsapi.org/v2/everything?q=Bitcoin&from="
secondpart = "&sortBy=popularity&apiKey=6c56cace4bdc41aab2a4832a3ef9d3f7"
translator = Translator()
text = get_text(url)
result = translator.translate(text, dest='ru',src='auto')
#print(result)
current_date = date.today()
resultString = firstpart + str(current_date) + secondpart
#print(resultString)
print(result)

if text[:5] == "":

    print(result)
else:
    print("No translate here")
# print(text)
#print(text[:19900])  # Первые 100 символов из строки
