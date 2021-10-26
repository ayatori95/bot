from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


driver.get('https://web.whatsapp.com/')
time.sleep(30)


def bot():
    try:
        #identifies the green ball that signals unread message
        ball = driver.find_element_by_class_name('_23LrM')
        ball = driver.find_elements_by_class_name('_23LrM')
        click_ball = ball[-1]
        action_ball = webdriver.ActionChains(driver)
        action_ball.move_to_element_with_offset(click_ball, 0, -20)
        action_ball.click()
        action_ball.perform()
        action_ball.click()
        action_ball.perform()
        #view and return the name or number of the client
        cell_client = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
        cell_final = cell_client.text
        print(cell_final)
        #view the last message and return it
        all_messagens = driver.find_element_by_class_name('_22Msk')
        all_messagens_txt = [e.text for e in all_messagens]
        msg = all_messagens_txt[-1]
        print (msg)
        #reply to client message
        text_camp = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div[1]/div[2]/div[1]/div/div[2]')
        action_camp = webdriver.ActionChains(driver)
        action_camp.move_to_element_with_offset(text_camp)
        action_camp.click()
        time.sleep(10)
        text_camp.send_keys('oi', Keys.ENTER)

    except:
            print('buscando novas mensagens')
            time.sleep(10)
while True:
    bot()
