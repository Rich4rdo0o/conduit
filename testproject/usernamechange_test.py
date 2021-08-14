from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True


def test_username_change():
    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "http://localhost:1667/#/"

    driver.get(url)
    time.sleep(3)

    # test data
    name = 'testuser2'
    email = 'testuser2@example.com'
    pw = 'Abcd123$'
    new_name = 'kiskutya'

    # TC05 - change username
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
    # checking logged in username
    username = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    assert username.text == name
    # can be a problem if the name was already changed
    # changing name
    settings = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a')
    settings.click()
    time.sleep(3)
    current_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
    current_name.clear()
    current_name.send_keys(new_name)
    update_settings = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/button')
    update_settings.click()
    time.sleep(4)
    change_success_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div')
    change_success_btn.click()
    time.sleep(4)
    # checking changed name
    home_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
    home_page.click()
    time.sleep(3)
    username = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    assert username.text == new_name
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()
    # could log in again to check if the new name is still saved, but I know it works from manual tests
    time.sleep(1)
    driver.close()
