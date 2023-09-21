import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09MSRJ97Y/ref=sr_1_5?crid=3KEBCMGKRNFG6&keywords=macbook+pro&qid=1689777643&sprefix=mac%2Caps%2C513&sr=8-5"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price.replace("$", "").replace(",", ""))
print(price_as_float)

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 3000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("minhdq1611@gmail.com",  "lhtuyqndqxfvoauw")
        connection.sendmail(
            from_addr="minhdq1611@gmail.com",
            to_addrs= "minhdq1611@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )