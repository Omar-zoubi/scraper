import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
def get_citation_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    key_word = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    return len(key_word)


fun=get_citation_needed_count(URL)
print(fun)

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    key_word = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    sentence_list = []
    count = 0
    for i  in key_word:
        if count == 0:
            sentence_list.append(i.parent.text)
            count = 1
        else:
            if i.parent.text in sentence_list:
                continue
            else:
                sentence_list.append(i.parent.text)
                count = count + 1
    formated = '\n'.join(sentence_list)
    return formated

fun2= get_citations_needed_report(URL)
print(fun2)    