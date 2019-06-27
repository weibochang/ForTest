from selenium import webdriver
from PIL import Image
from YDMHTTP import get_image_str


def seleniun_login(driver):
    driver.get('http://www.chaorendama.com/login.aspx?v=2')
    driver.find_element_by_id('txtUser').send_keys('七月的风')
    driver.find_element_by_id('txtPass').send_keys('123qweQWE')
    img = driver.find_element_by_id('img')
    get_login_img(img)
    code = get_verifyImg_str()
    driver.find_element_by_id('verifycode1').send_keys(code)
    driver.find_element_by_class_name('dl_an').click()
    # driver.find_element_by_xpath('//div[@class="dl_an"]')


def get_login_img(simg):
    location = simg.location
    print(location)
    size = simg.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    driver.save_screenshot('full_screen.png')
    # img_png = Image.open('full_screen.png')
    print(left,top,right,bottom)
    # time.sleep(5)
    img_png = Image.open('full_screen.png').crop((int(left), int(top), int(right), int(bottom)))
    img_png.save('full_screen.png')
    return img_png

def get_verifyImg_str():
    result = get_image_str('full_screen.png',2002)
    return result

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path='/home/cwb/文档/driver/Firefox/geckodriver')
    seleniun_login(driver)