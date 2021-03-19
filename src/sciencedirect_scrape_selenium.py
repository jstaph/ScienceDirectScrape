from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen, Request
from http.cookiejar import CookieJar
import re
import os
from selenium.webdriver.common.keys import Keys
import pathlib
from tqdm import tqdm
import requests
import gzip
import pickle
import unittest
from selenium import webdriver
import time
from os import walk
from urllib.request import urlopen


f = []
mypath = r"C:\\Users\\lanka\\Desktop\\Lab\\DARPA\\Scrape_Web\\Updated_Downloads\\Journal of Business Research"
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
# print(f[0])
print("downloaded folder has", len(f))

cj = CookieJar()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/80.0.3987.132 Safari/537.36"
}

pdf_urls = []
issue_urls_unrefined = []
issue_urls = []
start_vol = 62
end_vol = 105

for i in range(start_vol + 1, end_vol + 1):
    # print(i)
    issue_urls_unrefined.append(
        "https://www.sciencedirect.com/journal/journal-of-business-research/vol/{0}/suppl/C".format(
            i
        )
    )

for ii in range(start_vol, end_vol + 1):
    # print(i)
    for j in range(1, 13):
        issue_urls_unrefined.append(
            "https://www.sciencedirect.com/journal/journal-of-business-research/vol/{0}/issue/{1}".format(
                ii, j
            )
        )

print(len(issue_urls_unrefined))
print(issue_urls_unrefined)

# for i in issue_urls_unrefined:
#     request = requests.get(i)
#     if request.status_code == 200:
#         issue_urls.append(i)
#     else:
#         continue
#     print(len(issue_urls))
issue_urls = issue_urls_unrefined

print(len(issue_urls))

total_count = 0
for i in issue_urls:

    req = Request(url=i, headers=headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html)
    # print(i)
    for link in soup.findAll(
        "a",
        attrs={
            "class": "anchor pdf-download u-margin-l-right text-s",
            "target": "_blank",
        },
    ):
        pdf_urls.append("https://www.sciencedirect.com" + link.get("href"))
        pdf_urls = list(set(pdf_urls))
print("total urls", len(pdf_urls))


def Filter(string, substr):
    return [str for str in string if any(sub in str for sub in substr)]


pdf_urls_downloaded = Filter(pdf_urls, f)
print("urls for downloaded pdfs", len(pdf_urls_downloaded))

pdf_urls_new = list(set(pdf_urls).difference(pdf_urls_downloaded))
print("number of new downloads to be done", len(pdf_urls_new))

j = 0
for i in range(len(pdf_urls_new)):
    i = j
    if i > len(pdf_urls_new) - 1:
        break
    options = webdriver.ChromeOptions()
    pref = {"plugins.always_open_pdf_externally": True}
    options.add_experimental_option("prefs", pref)
    # options.add_argument("--test-type")
    # options.binary_location = "/usr/bin/chromium"
    browser = webdriver.Chrome(
        executable_path=r"C:\\Users\\lanka\Desktop\\Lab\\DARPA\\Scrape_Web\\chromedriver_win32\\chromedriver.exe",
        chrome_options=options,
    )
    browser.get(pdf_urls_new[i])
    # time.sleep(1)
    # search_form = browser.find_element_by_id("acceptTC")
    # search_form.click()

    if i + 1 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab2');")
        browser.switch_to.window("tab2")
        browser.get(pdf_urls_new[i + 1])

    if i + 2 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab3');")
        browser.switch_to.window("tab3")
        browser.get(pdf_urls_new[i + 2])

    if i + 3 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab4');")
        browser.switch_to.window("tab4")
        browser.get(pdf_urls_new[i + 3])

    if i + 4 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab5');")
        browser.switch_to.window("tab5")
        browser.get(pdf_urls_new[i + 4])

    if i + 5 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab6');")
        browser.switch_to.window("tab6")
        browser.get(pdf_urls_new[i + 5])

    if i + 6 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab7');")
        browser.switch_to.window("tab7")
        browser.get(pdf_urls_new[i + 6])

    if i + 7 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab8');")
        browser.switch_to.window("tab8")
        browser.get(pdf_urls_new[i + 7])

    if i + 8 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab9');")
        browser.switch_to.window("tab9")
        browser.get(pdf_urls_new[i + 8])

    if i + 9 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab10');")
        browser.switch_to.window("tab10")
        browser.get(pdf_urls_new[i + 9])

    if i + 10 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab11');")
        browser.switch_to.window("tab11")
        browser.get(pdf_urls_new[i + 10])

    if i + 11 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab12');")
        browser.switch_to.window("tab12")
        browser.get(pdf_urls_new[i + 11])

    if i + 12 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab13');")
        browser.switch_to.window("tab13")
        browser.get(pdf_urls_new[i + 12])

    if i + 13 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab14');")
        browser.switch_to.window("tab14")
        browser.get(pdf_urls_new[i + 13])

    if i + 14 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab15');")
        browser.switch_to.window("tab15")
        browser.get(pdf_urls_new[i + 14])

    if i + 15 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab16');")
        browser.switch_to.window("tab16")
        browser.get(pdf_urls_new[i + 15])

    if i + 16 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab17');")
        browser.switch_to.window("tab17")
        browser.get(pdf_urls_new[i + 16])

    if i + 17 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab18');")
        browser.switch_to.window("tab18")
        browser.get(pdf_urls_new[i + 17])

    if i + 18 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab19');")
        browser.switch_to.window("tab19")
        browser.get(pdf_urls_new[i + 18])

    if i + 19 <= len(pdf_urls_new) - 1:
        browser.execute_script("window.open('about:blank', 'tab20');")
        browser.switch_to.window("tab20")
        browser.get(pdf_urls_new[i + 19])

    # print(search_form)
    j = i + 20
    # search_form.send_keys('real python')
    # search_form.click()
    time.sleep(4)
    browser.quit()
    break
