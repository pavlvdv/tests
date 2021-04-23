import time


class Registration:
    def __init__(self, driver):
        self.driver = driver

    # кнопка Приступайте
    def button_registration(self):
        driver = self.driver
        button_registration = driver.find_element_by_link_text("Приступайте")
        button_registration.click()

    # поле email
    def field_email(self, email):
        driver = self.driver
        field_email = driver.find_element_by_id("email")
        field_email.click()
        field_email.send_keys(email)

    # поле имя
    def field_name(self, name):
        driver = self.driver
        field_name = driver.find_element_by_id("username")
        field_name.click()
        field_name.send_keys(name)

    # поле пароль
    def field_password(self, password):
        driver = self.driver
        field_pass = driver.find_element_by_id("password")
        field_pass.click()
        field_pass.send_keys(password)

    # кнопка Создать учётную запись
    def button_create(self):
        driver = self.driver
        button_create = driver.find_element_by_css_selector("div.card.logged-out-form__footer.is-blended > button")
        button_create.click()

    # успешная регистрация
    def validation_successfully(self):
        time.sleep(1)
        element = self.driver.find_element_by_css_selector(".formatted-header__title")
        assert element.text == "Давайте найдём домен для вашего сайта!"

    # валидатор емаил
    def validation_email(self, text_validation):
        time.sleep(1)
        element = self.driver.find_element_by_css_selector(".form-input-validation:nth-child(3)")
        assert element.text == text_validation

    # пустой емаил
    def validation_bad_email_empty(self):
        self.validation_email("Чтобы получать сообщения, укажите действующий адрес электронной почты.")

    # некорректный емаил
    def validation_bad_email(self):
        self.validation_email("Чтобы получать наши сообщения, укажите действующий адрес электронной почты.")

    # повторный емаил
    def validation_bad_email_repeat(self):
        self.validation_email("Выберите другой адрес электронной почты. Этот адрес недоступен. "
                              "Если это вы, войдите в вашу учётную запись.")

    # валидатор имя
    def validation_name(self, text_validation):
        time.sleep(1)
        element = self.driver.find_element_by_css_selector(".form-input-validation:nth-child(6)")
        assert element.text == text_validation

    # пустое имя
    def validation_bad_name_empty(self):
        self.validation_name("Введите выбранное имя пользователя.")

    # имя из цифр
    def validation_bad_name_numbers(self):
        self.validation_name("Добавьте хотя бы одну букву.")

    # сушествующие имя
    def validation_bad_name_repeat(self):
        self.validation_name("Извините, это имя пользователя уже существует! "
                             "Если это вы, войдите в вашу учётную запись.")

    # валидатор пароль
    def validation_password(self, text_validation):
        time.sleep(1)
        element = self.driver.find_element_by_css_selector(".form-input-validation:nth-child(9)")
        assert element.text == text_validation

    # пустой пароль
    def validation_bad_password_empty(self):
        self.validation_password("Не забудьте ввести пароль.")

    # короткий пароль
    def validation_bad_password_short(self):
        self.validation_password("Пароль должен состоять хотя бы из 6 символов.")

    # простой пароль
    def validation_bad_password_simple(self):
        self.validation_password("Это очень распространенный пароль. "
                                 "Выберите более сложный пароль, который будет трудно угадать.")
