import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from time import sleep
from selenium.webdriver.common.by import By


def getSolded(link):
    driver.get(link)  # Truy cập trang sản phẩm
    sleep(2)  # Đợi trang load hoàn tất (có thể dùng WebDriverWait thay thế)

    try:
        sold = driver.find_element(
            By.CSS_SELECTOR, ".product-name .quantity-sale").text
    except NoSuchElementException:
        print(f"No Such Element Exception on {link}")
        sold = "No quantity sale"

    driver.back()  # Quay lại trang danh mục
    sleep(2)  # Đợi trang load lại

    return sold


# Mở trình duyệt Chrome
driver = webdriver.Chrome()
driver.get("https://www.thegioididong.com/laptop#c=44&o=13&pi=16")
sleep(10)

# Tìm phần tử bằng CSS Selector
elems = driver.find_elements(
    By.CSS_SELECTOR, ".item.__cate_44 > [href]")

# Lấy thông tin sản phẩm
titles = [elem.get_attribute(
    'data-name') if elem.get_attribute('data-name') else "Unknown" for elem in elems]
links = [elem.get_attribute('href') if elem.get_attribute(
    'href') else "No Link" for elem in elems]
brands = [elem.get_attribute('data-brand') if elem.get_attribute(
    'data-brand') else "No brand" for elem in elems]

solds = [getSolded(link) for link in links]

elem_imgs = driver.find_elements(
    By.CSS_SELECTOR, ".item.__cate_44 > [href] .item-img.item-img_44 .thumb")
imgs = []
for elem_img in elem_imgs:
    src = elem_img.get_attribute('src')
    if src:
        imgs.append(src)
    elif elem_img.get_attribute('data-src'):
        imgs.append(elem_img.get_attribute('data-src'))
    else:
        imgs.append("No image")


elem_prices = driver.find_elements(
    By.CSS_SELECTOR, ".item.__cate_44 > [href] .price")
prices = [
    elem_price.text if elem_price.text else "No price" for elem_price in elem_prices]


ram_list, item_idx, rom_list = [], [], []
for i in range(1, len(titles)+1):
    try:
        ram = driver.find_element(
            "xpath", "/html/body/div[7]/section[5]/div[1]/ul/li[{}]/a/div[3]/span[1]".format(i))
        ram_list.append(ram.text)
        rom = driver.find_element(
            "xpath", "/html/body/div[7]/section[5]/div[1]/ul/li[{}]/a/div[3]/span[2]".format(i))
        rom_list.append(rom.text)
        print(i)
        item_idx.append(i)
    except NoSuchElementException:
        print("No Such Element Exception Rom Ram " + str(i))
        rom_list.append("No Rom")
        item_idx.append(i)

elem_rates = driver.find_elements(
    By.CSS_SELECTOR, ".item.__cate_44 > .rating_Compare.has_compare .vote-txt")
rates = [
    elem_rate.text if elem_rate.text else "No rate" for elem_rate in elem_rates]

# Tạo dataframe chứa các thông tin title, price, link product, img product
df1 = pd.DataFrame(list(zip(titles, brands, prices, links, imgs, ram_list, rom_list, rates, solds)), columns=[
                   'title', 'brand', 'price', 'link_item', 'link_img', 'ram', 'rom', 'rate', 'Lượt bán'])
df1['index_'] = np.arange(1, len(df1) + 1)


discount_list, discount_idx, discount_percent_list = [], [], []
for i in range(1, len(titles)+1):
    try:
        discount = driver.find_element(
            "xpath", "/html/body/div[7]/section[5]/div[1]/ul/li[{}]/a/div[4]/p".format(i))
        discount_list.append(discount.text)
    except NoSuchElementException:
        print("No Such Element Exception discount " + str(i))
        discount_list.append("No discount info")
    try:    
        discount_percent = driver.find_element(
            "xpath", "/html/body/div[7]/section[5]/div[1]/ul/li[{}]/a/div[4]/span".format(i))
        discount_percent_list.append(discount_percent.text)
    except NoSuchElementException:
        print("No Such Element Exception discount percent " + str(i))
        discount_percent_list.append("No discount percent")
    print(i)
    discount_idx.append(i)


df2 = pd.DataFrame(list(zip(discount_idx, discount_list, discount_percent_list)), columns=[
                   'discount_index', 'original price', 'discount percent'])

df3 = df1.merge(df2, how='left', left_on='index_', right_on='discount_index')

# Đóng trình duyệt sau khi hoàn thành
driver.quit()

df3.to_csv("laptopProduct.csv", index=False, encoding="utf-8-sig")
