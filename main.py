from bs4 import BeautifulSoup
import requests

url1 = 'https://brych.pythonanywhere.com/works.html'

response = requests.get(url1)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

atags = soup.find_all('a')
h3s = soup.find_all('h3')
ptags = soup.find_all('p')

def search(language):
    count = 0
    for x in range(0, len(atags)):
        if language.lower() in atags[x].get_text().lower():
            print(atags[x].find_previous_sibling('h3').get_text())
            print(atags[x].find_previous_sibling('p').get_text())
            print(atags[x].get('href'))
            count += 1       

    for y in range(0, len(h3s)):
        if language.lower() in h3s[y].get_text().lower():
            print(h3s[y].get_text())
            print(h3s[y].find_next_sibling('p').get_text())
            print(h3s[y].find_next_sibling('a').get('href'))
            count += 1

    for z in range(0, len(ptags)):
        if language.lower() in ptags[z].get_text().lower():
            print(ptags[z].find_previous_sibling('h3').get_text())
            print(ptags[z].get_text())
            print(ptags[z].find_next_sibling('a').get('href'))
            count += 1
        
    if count == 0:
        print("No results for this tech :-( Try: Python, JavaScript, PHP, SQL, REACT, Playwright, Flask) " + language)


search('flask')





