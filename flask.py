from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    language = request.args.get('language')
    
    url1 = 'https://brych.pythonanywhere.com/works.html'
    response = requests.get(url1)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    atags = soup.find_all('a')
    h3s = soup.find_all('h3')
    ptags = soup.find_all('p')

    results = []

    for x in atags:
        if language.lower() in x.get_text().lower():
            results.append({
                'title': x.find_previous_sibling('h3').get_text(),
                'description': x.find_previous_sibling('p').get_text(),
                'link': x.get('href')
            })
            
    for y in h3s:
        if language.lower() in y.get_text().lower():
            results.append({
                'title': y.get_text(),
                'description': y.find_next_sibling('p').get_text(),
                'link': y.find_next_sibling('a').get('href')
            })

    for z in ptags:
        if language.lower() in z.get_text().lower():
            results.append({
                'title': z.find_previous_sibling('h3').get_text(),
                'description': z.get_text(),
                'link': z.find_next_sibling('a').get('href')
            })

    if not results:
        return jsonify({"message": f"No results for this tech :-( Try: Python, JavaScript, PHP, SQL, REACT, Playwright, Flask) {language}"})

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
