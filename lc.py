from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','follow your page','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] 

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)
driver.find_element_by_name('username').send_keys('dlopoelegssgvs') #replace with your insta username
driver.find_element_by_name('password').send_keys('insta232') #replace with your password
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(9)
driver.get('https://www.instagram.com/kichchasudeepa/') #replace with your targeted account url where you want to put auto like & cmt
sleep(11)
driver.find_element_by_class_name('_aagw').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
next_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
sleep(3)
like=driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//textarea').send_keys(random.choice(commentsDict))
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aidk"]//button[@type="submit"]').click()
sleep(3)
driver.close()
#here i added upto 25 posts auto likes & comments if you want another 25 posts auto likes & comments means then copy line from 35 to 282 and paste in 283 line(open notepad ++ for no line)


