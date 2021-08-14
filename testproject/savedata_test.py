from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True


def test_save_data():
    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    name = 'testuser1'
    email = 'testuser1@example.com'
    pw = 'Abcd123$'
    old_post_title = 'test post'

    # TC09 - Save data from page
    # login
    sign_in = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    sign_in.click()
    time.sleep(3)
    email_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    pw_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    email_field.send_keys(email)
    pw_field.send_keys(pw)
    sign_in_btn.click()
    time.sleep(4)
    # choose a post
    a_post = driver.find_element_by_class_name('preview-link')
    a_post.click()
    time.sleep(3)
    data = driver.find_element_by_class_name('col-xs-12')
    # print(data.text)
    # save article to file
    with open('save_down.txt', 'w') as output:
        output.write(data.text)
    # checking whether correct data was saved
    with open('save_down.txt') as f:
        saved = f.read()
    assert data.text == saved
    # print(data.text)
    # print(saved)
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    time.sleep(1)
    driver.close()
