from bs4 import BeautifulSoup
# import lxml

with open("website.html", errors="ignore") as file:
    contents = file.read()

soup = BeautifulSoup(markup=contents, features='html.parser')

# company_url = soup.select(selector=".heading")
# another_company_url = soup.find_all(name="h3", class_="heading")
# # headings = soup.select(".heading")
# # print(headings)
# print(company_url)
# print(another_company_url)

# form_tag = soup.find(name="input")
# print(form_tag.get(key="name"))

# print(soup.find_all(name="h3", class_="heading"))

