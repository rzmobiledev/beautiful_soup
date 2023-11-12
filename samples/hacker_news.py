from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(markup=yc_webpage, features="html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    texts = article_tag.find(name="a")
    article_texts.append(texts.getText())
    article_links.append(texts.get(key="href"))

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# for highest_article_vote in range(len(article_upvote)):
#     if article_upvote[highest_article_vote] == max(article_upvote):
#         print(article_texts[highest_article_vote])
#         print(article_links[highest_article_vote])
#         print(article_upvote[highest_article_vote])

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)