from selenium import webdriver
import bs4

url ="https://www.datacamp.com/tracks/machine-learning-scientist-with-python"

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

btn = driver.find_element_by_xpath("""//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[1]/div/div/div[4]/button""")
btn.click()

bs = bs4.BeautifulSoup(driver.page_source, features="html.parser")

courses = bs.select("#gatsby-focus-wrapper > div > div.container.css-93pq91 > div.col-md-8 > div > div > div > div.css-2cldv8 > a")
courseList = []
for c in courses:
    link = c.attrs["href"]
    title = c.select_one("h4").getText().strip()
    desc = c.select_one("p").getText().strip()
    courseList.append({"link": link, "title": title, "desc": desc})
print(len(courseList))