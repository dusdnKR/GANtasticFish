import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 자동으로 받아오기
options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 크롤링할 페이지 링크(수정)
driver.get('https://www.google.com/search?q=betta+fish&sxsrf=AJOqlzV6S6OSnM_jyLIzJ0uN_8pi4bp7Gw:1679216474117&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiQ9MLr0Of9AhXnglYBHRQeA8YQ_AUoAXoECAgQAw&biw=1066&bih=1040&dpr=0.9')

# 원하는 사진 장수(count) 입력
count = 0
while count < 1500:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # 페이지에 있는 사진들 크롤링
    images = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
    for image in images:
        try:
            img_url = image.get_attribute('src')
            # "betta_fish_images_1500" 폴더(수정)에 내 이미지 저장
            urllib.request.urlretrieve(img_url, f'betta_fish_images_1500/{count}.jpg')
            # 잘 다운받고 있는지 확인(없어도 됨)
            print(f'Downloaded image {count}')
            count += 1

            # count 횟수 다 채우면 종료
            if count == 1500:
                break
        except:
            pass

driver.quit()