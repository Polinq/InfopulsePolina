from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/user/Documents/chromedriver')
driver.get("https://stage.subj.ua/")
product_page = driver.find_element_by_class_name("sc-hqyNC").click() # карточка товара

driver.get("https://stage.subj.ua/catalog/product-page/33146")
# button = driver.find_element_by_class_name("fqBEVH")
button.click() # кнопка "В корзину"
t = time.sleep(10)
# driver.find_element_by_class_name("sc-VigVT").click() # Крестик в попапе
driver.find_element_by_class_name("sc-fHSTwm").click() # иконка корзины

driver.get("https://stage.subj.ua/checkout/cart")
driver.find_element_by_class_name("fqBEVH").click() # кнопка "Заказать"

driver.get("https://stage.subj.ua/checkout/delivery")
driver.find_element_by_class_name("sc-gbOuXE").click() # радиабаттон "Доставка на склад новой почты"


elm = driver.find_element_by_name("receiver_full_name") # нпоиск поля ФИО
elm.click() # нажатие в поле ФИО
elm.send_keys("Фамилия Имя Отвество") # ФИО

tel = driver.find_element_by_name("receiver_phone") # номер телефона
tel.click() # клик в поле номер телефона
tel.send_keys("1234567890")

# city = driver.find_element_by_class_name("kDMTkp") # поиск поля со списком городов
# ddm = Select(driver.find_element_by_class_name("sc-VigVT")) # поиск стрелочки раскрывающей список
# ddm.click() # нажатие на стелку раскрывающею список
# ddm.Select_by_value('1').click()
#
#
# city.send_keys("Авангард") # список городов
# city.send_keys(Keys.ENTER) # ENTER
#
# elem = driver.find_element_by_class_name("sc-kGXeez").click() # номер отделения
# elem.send_keys("Відділення № 1: вул. Ангарська, 13/1") # список отделений
# elem.send_keys(Keys.ENTER) # ENTER

# driver.find_element_by_class_name("sc-fjdhpX").click() # кнопка "Продолжить"
# driver.find_element_by_class_name("sc-VigVT").click() # банковский перевод
driver.find_element_by_class_name("sc-fjdhpX").click() # кнопка "Изменить заказ"
driver.find_element_by_class_name("sc-fjdhpX").click() # нажатие на "крестик" для удаления
driver.find_element_by_class_name("sc-iBmynh").click() # нажатие на логотип

driver.quit()


