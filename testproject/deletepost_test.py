from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def test_delete_post():
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    email = 'testuser1@example.com'
    pw = 'Abcd123$'
    # TC07 - Delete post
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
    old_post_numbers1 = len(driver.find_elements_by_xpath('//div//a//p'))
    old_post = driver.find_element_by_xpath('//div//a//p')
    old_post.click()
    time.sleep(4)
    delete_post = driver.find_element_by_xpath('//div//span//button')
    delete_post.click()
    time.sleep(4)
    # checking the error message, have to write a bug ticket about it
    error_message = driver.find_element_by_class_name('swal-text')
    assert error_message.text == 'Something went wrong whilst trying to delete the article.'
    error_ok_btn = driver.find_element_by_class_name('swal-button-container')
    error_ok_btn.click()
    time.sleep(3)
    home_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
    home_page.click()
    time.sleep(3)
    # checking whether the post was deleted or not
    old_post_numbers2 = len(driver.find_elements_by_xpath('//div//a//p'))
    # checking the number of posts with the given title
    # if there is -1 that means the correct post was deleted
    assert (old_post_numbers1 - 1) == old_post_numbers2
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    time.sleep(1)
    driver.close()
