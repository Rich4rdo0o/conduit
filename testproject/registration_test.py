from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True


def test_registration():
    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    name = 'tesztelek1'
    email = 'teszt1@elek.com'
    pw_normal = 'Abcd1234'
    pw_weak = 'abc123'

    # TC01 - registration
    sign_up_menu = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a')
    sign_up_menu.click()
    time.sleep(3)
    # registration with empty data
    sign_up_btn = driver.find_element_by_xpath('//button')
    sign_up_btn.click()
    time.sleep(3)
    username_error = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
    assert username_error.text == 'Username field required.'
    accept_btn1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    accept_btn1.click()
    time.sleep(3)
    # registration with weak password
    username_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    password_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')
    username_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(pw_weak)
    sign_up_btn.click()
    time.sleep(4)
    password_error = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
    assert password_error.text == 'Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.'
    accept_btn2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    accept_btn2.click()
    time.sleep(3)
    # registration with correct data
    username_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(pw_normal)
    sign_up_btn.click()
    time.sleep(4)
    # welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]')
    # assert welcome.text == 'Welcome!'
    accept_btn3 = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div')
    accept_btn3.click()
    time.sleep(4)
    # checking whether the user is logged in
    user = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    assert user.text == name
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    time.sleep(1)
    driver.close()
