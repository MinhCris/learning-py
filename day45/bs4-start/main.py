from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
    m =file.read()

soup = BeautifulSoup(m, "html.parser")
#print(soup.p)    in ra taats ca p trong html
#all tag a = soup.find_all(name="a") tim tat ca a trong html

#eading = soup.find(name="h1", id = "name") tim cu the id name o h1

# for tag in all tag a
#     print(tag.getText())    In ra text
#     print(tag.get("href"))  In ra href
# Tim class cu the thi phai laf class_

#soup.find_all(name =" a")  tim tat ca the co ten "a"