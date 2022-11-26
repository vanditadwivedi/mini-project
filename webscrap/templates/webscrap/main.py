from typing import List

from selenium import webdriver
import time
import pandas as pd
# import os

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

url1 = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analysis&location=Kakori%2C%20Uttar%20Pradesh%2C%20India&geoId=106431974&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
driver = webdriver.Chrome(executable_path="C:\\Users\\AYUSHI\\Downloads\\chromedriver.exe")
driver.get(url1)
driver.implicitly_wait(10)

y = driver.find_elements(By.CLASS_NAME, 'results-context-header__job-count')[0].text  # access element by class name
# print(y)
n = pd.to_numeric(y)  # convert string to numeric
print(n)
i = 2
while i <= 16:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    try:
        x = driver.find_element(By.xpath("//button[@aria-label='Load more results']"))
        driver.execute_script("arguments[0].click();", x)
        time.sleep(4)
    except:
        pass
        time.sleep(4)

companyName = []
for j in range(n):
    try:
        company = driver.find_elements(By.CLASS_NAME, "base-search-card__subtitle")[j].text
        companyName.append(company)
        # print(company)
    except IndexError:
        print("done")


# to print title
titleName = []
for j in range(n):
    try:
        title = driver.find_elements(By.CLASS_NAME, "base-search-card__title")[j].text
        titleName.append(title)
        # print(titleName)
    except IndexError:
        print("done")

companyFinal = pd.DataFrame(companyName, columns=['company'])

titleFinal = pd.DataFrame(titleName, columns=['title'])

final = companyFinal.join(titleFinal)
# print(final)
# final.to_csv('linkdinjobdetails.csv')

Linklist = []
findlink = driver.find_elements(By.CLASS_NAME, "base-card__full-link")
for k in findlink:
    Linklist.append(k.get_attribute('href'))
    # print(Linklist)

linkFinal = pd.DataFrame(Linklist, columns=['company Link'])

final1 = final.join(linkFinal)
print(final1)
final1.to_csv('linkdinjobdetails.csv')
