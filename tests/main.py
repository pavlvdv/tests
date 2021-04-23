import random

from selenium import webdriver
from pageObjects.registration import Registration

# тестовые данные
emailRnd = "test" + str(random.randint(1111111, 9999999)) + "@test.ru"
nameRnd = "test" + str(random.randint(1111111, 9999999))
passRnd = "tEst" + str(random.randint(1111111, 9999999))

url = "https://wordpress.com/ru/"


class TestRegistration:

    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('start-maximized')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def teardown_method(self):
        self.driver.quit()

    def test_positive(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_email(emailRnd)
        r.field_name(nameRnd)
        r.field_password(passRnd)
        r.button_create()
        r.validation_successfully()

    def test_negative_01(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_email("fgsdfgs")
        r.button_create()
        r.validation_bad_email()

    def test_negative_02(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_email(" ")
        r.button_create()
        r.validation_bad_email_empty()

    def test_negative_03(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_email("guest@gmail.com")
        r.button_create()
        r.validation_bad_email_repeat()

    def test_negative_04(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_name(" ")
        r.button_create()
        r.validation_bad_name_empty()

    def test_negative_05(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_name("11111")
        r.button_create()
        r.validation_bad_name_numbers()

    def test_negative_06(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_name("guest")
        r.button_create()
        r.validation_bad_name_repeat()

    def test_negative_07(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_password("111")
        r.button_create()
        r.validation_bad_password_short()

    def test_negative_08(self):
        r = Registration(self.driver)
        r.button_registration()
        r.field_password("1234567")
        r.button_create()
        r.validation_bad_password_simple()

    def test_negative_09(self):
        r = Registration(self.driver)
        r.button_registration()
        r.button_create()
        r.validation_bad_email_empty()
        r.validation_bad_name_empty()
        r.validation_bad_password_empty()
