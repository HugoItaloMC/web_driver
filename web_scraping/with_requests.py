import requests
from lxml import html

headers={
    "user-agent": "Mozilla/5.0 (X11, Linux X86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chormium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}
url = 'https://www.wikipedia.org/'

response = requests.get(url,  # A Url
                        headers=headers)  # Meet in from requester this header

parser = html.fromstring(response.text)

element_from_id = parser.get_element_by_id('js-link-box-es')  # Search how ID element
print(element_from_id.text_content())  # Output content in element (TAG)

element_from_path = parser.xpath("//a[@id='js-link-box-es']/strong/text()")  # Search how xpath
print(element_from_path)  # output xpath

# Get from `div` a  content with common classes

all_elements_from_path = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")  # Search from xpath
print(all_elements_from_path)
