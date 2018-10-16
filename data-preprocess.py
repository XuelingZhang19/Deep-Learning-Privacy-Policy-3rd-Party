from bs4 import BeautifulSoup
import bs4

htmfile = '/Users/xueling/Desktop/Deep learning/OPP-115/sanitized_policies/1017_sci-news.com.html'
html = open(htmfile, 'r', encoding='utf-8')
htmlpage = html.read()
soup = BeautifulSoup(htmlpage.strip(), 'html.parser')
print(soup.text)
