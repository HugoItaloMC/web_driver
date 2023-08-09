import requests
from bs4 import BeautifulSoup
#  Read web-site :`https://stackoverflow.com/questions` Get a first page posts from main this questions
headers={
    "user-agent": "Mozilla/5.0 (X11, Linux X86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chormium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url = 'https://stackoverflow.com/questions'

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text)

main_div = soup.find(id="questions")  # Get main div from `id`
childs_div = main_div.find_all('div', class_='s-post-summary')  # Get child div from `class`

for element in childs_div:
    text_from_title = element.find('h3').text  # Get content in element `h3`
    text_from_content = element.find(class_='s-post-summary--content-excerpt').text  # Get content in `class`
    print(text_from_title)
    print(text_from_content.replace('\n', '').replace('\r', ''))  # Output how cleanin up text
