import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests

def get_data(url):
    # s = Service(r"C:\Users\AI\Desktop\parser\lesson6selenium\geckodriver.exe")
    # options = webdriver.FirefoxOptions()
    # options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
    # driver = webdriver.Firefox(options=options,service=s)


    # try:

    #     driver.get(url=url)
    #     time.sleep(5)

    #     with open("index1.html", "w", encoding="utf-8") as file:
    #         file.write(driver.page_source)

    # except Exception as ex:
    #     print(ex)

    # finally:
    #     driver.close()
    #     driver.quit()
    with open("lesson6selenium/index1.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    titles = soup.findAll('a', id="video-title-link")

    for title in titles:
        title = title.get("title")
        print(title)



def main():
    get_data("https://www.youtube.com/@PythonToday/videos")

if __name__ == "__main__":
    main()