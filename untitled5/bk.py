import requests
from bs4 import BeautifulSoup


def get_rec():
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    recepts = soup.findAll('div', class_='post-name')
    ingr = soup.findAll('div', {"class": "post_c"})
    ingr_data = []
    i = 0
    rec = {}
    for el in ingr:
        d={}
        d['categ']=el.find('a').getText()
        d['ingr']=el.findAll('li', {"itemprop": "ingredients"})
        ingr_data.append(d)
        i = i + 1
    i = 0
    for block in recepts:
        rec_data = block.find('a')
        rec['href'] = rec_data['href']  ##ссылка на стр с рецептом
        rec['title'] = rec_data.getText()
        print(rec['title'], "\n Категория: \n  ",ingr_data[i]['categ'])
        for u in ingr_data[i]['ingr']:
            rec['ing'] = u.getText()
            print(rec['ing'], " ")
        i = i + 1
        print("   ")
        get_instr(rec['href'])


def get_instr(href):
    t = requests.get(href)
    html1 = t.text
    soup1 = BeautifulSoup(html1, 'html.parser')
    ##comm=soup1.find('div', id_="dle-comments-list")
    instruct = soup1.find('ul', itemprop="recipeInstructions").findAll('li')
    ##l =instruct.getText()
    rating = 0
    rating = soup1.find('li', class_='current-rating').getText()
    for n in instruct:

        f = n.findAll('div')
        for i in f:
         i.decompose()
        m = n.getText()
        print(m)
        ref = n.find('a')
        if ref is not None:
            print(ref['href'])
    print(f"Рейтинг:\n {rating}/100")
    comments = soup1.find('div', {"id": "dle-comments-list"})
    if comments is not None:
        print("Комментарии: \n")
        for com in comments.findAll('td', class_='comm'):
            print(com.getText())

for i in range(10):
    r=requests.get(f'https://www.jrati.ru/page/{i}/')
    get_rec()