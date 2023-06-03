from selenium.webdriver.common.by import By

class MainMenuLocators:
    # Кнопка Конструктор в главном меню
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[contains(text(),'Конструктор')]")
    # Кнопка Личный Кабинет в главном меню
    LK_BUTTON = (By.XPATH, ".//*[contains(text(),'Личный Кабинет')]")

class ConstructorLocators:
    # Заголовок страницы конструктора
    ASSEMBLE_BURGER_LABEL = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    # Кнопка секции булок
    ROLL_BUTTON = (By.XPATH, ".//*[contains(text(),'Булки')]")
    # Кнопка секции соусов
    SAUCE_BUTTON = (By.XPATH, ".//*[contains(text(),'Соусы')]")
    # Кнопка секции начинок
    TOPPING_BUTTON = (By.XPATH, ".//*[contains(text(),'Начинки')]")

    # Активная секция булок
    ROLL_DIV = (By.XPATH, ".//div[contains(@class, 'current')]/span[text()='Булки']")
    # Активная секция соусов
    SAUCE_DIV = (By.XPATH, ".//div[contains(@class, 'current')]/span[text()='Соусы']")
    # Активная секция начинок
    TOPPING_DIV = (By.XPATH, ".//div[contains(@class, 'current')]/span[text()='Начинки']")
    # Кнопка входа на странице конструктора
    LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти в аккаунт')]")

class RegistrationLocators:
    # Поле ввода имени на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    # Поле ввода почты на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    # Поле ввода пароля на странице регистрации
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    # Кнопка регистрации на странице регистрации
    REG_BUTTON = (By.XPATH, ".//*[contains(text(),'Зарегистрироваться')]")
    # Кнопка войти на странице регистрации
    LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти')]")
    # Сообщение, что пароль некорректен, на странице регистрации
    ERROR_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

class LoginLocators:
    # Заголовок страницы входа
    LOGIN_LABEL = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    # Поле ввода почты на странице входа
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    # Поле ввода пароля на странице входа
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    # Кнопка войти на странице входа
    LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти')]")
    # Кнопка регистрации на странице входа
    REG_BUTTON = (By.XPATH, ".//*[contains(text(),'Зарегистрироваться')]")
    # Кнопка восстановления пароля на странице входа
    RESTORE_PASSWORD_BUTTON = (By.XPATH, ".//*[contains(text(),'Восстановить пароль')]")
    # Сообщение, что пароль некорректен, на странице входа
    ERROR_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

class LkLocators:
    # Заголовок страницы личного кабинета
    PROFILE_LABEL = (By.XPATH, "//a[contains(text(),'Профиль')]")
    # Кнопка разлогиниться на странице личного кабинета
    LOGOUT_BUTTON = (By.XPATH, ".//*[contains(text(),'Выход')]")
    # Поле Логин в Профиле
    PROFILE_EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Логин')]/following-sibling::input")

class RestorePasswordLocators:
    # Кнопка войти на странице восстановления пароля
    LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти')]")




