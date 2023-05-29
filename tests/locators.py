from selenium.webdriver.common.by import By

class Locators:
    # Кнопка Конструктор в главном меню
    MAIN_MENU_CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[contains(text(),'Конструктор')]")
    # Кнопка Личный Кабинет в главном меню
    MAIN_MENU_LK_BUTTON = (By.XPATH, ".//*[contains(text(),'Личный Кабинет')]")

    # Заголовок страницы конструктора
    CONSTRUCTOR_PAGE_MAIN_LABEL = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    # Кнопка секции булок
    CONSTRUCTOR_PAGE_ROLL_BUTTON = (By.XPATH, ".//*[contains(text(),'Булки')]")
    # Кнопка секции соусов
    CONSTRUCTOR_PAGE_SAUCE_BUTTON = (By.XPATH, ".//*[contains(text(),'Соусы')]")
    # Кнопка секции начинок
    CONSTRUCTOR_PAGE_TOPPING_BUTTON = (By.XPATH, ".//*[contains(text(),'Начинки')]")
    # Активная секция булок
    CONSTRUCTOR_PAGE_ROLL_DIV = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1][contains(@class,'current')]")
    # Активная секция соусов
    CONSTRUCTOR_PAGE_SAUCE_DIV = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2][contains(@class,'current')]")
    # Активная секция начинок
    CONSTRUCTOR_PAGE_TOPPING_DIV = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3][contains(@class,'current')]")
    # Кнопка входа на странице конструктора
    CONSTRUCTOR_PAGE_LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти в аккаунт')]")

    # Заголовок страницы регистрации
    REG_PAGE_MAIN_LABEL = (By.XPATH, "//h2[contains(text(),'Регистрация')]")
    # Поле ввода имени на странице регистрации
    REG_PAGE_NAME_INPUT = (By.XPATH, ".//input[@name='name']")
    # Поле ввода почты на странице регистрации
    REG_PAGE_EMAIL_INPUT = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input")
    # Поле ввода пароля на странице регистрации
    REG_PAGE_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    # Кнопка регистрации на странице регистрации
    REG_PAGE_BUTTON = (By.XPATH, ".//*[contains(text(),'Зарегистрироваться')]")
    # Кнопка войти на странице регистрации
    REG_PAGE_LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти')]")
    # Сообщение, что пароль некорректен, на странице регистрации
    REG_PAGE_ERROR_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    # Заголовок страницы входа
    LOGIN_PAGE_MAIN_LABEL = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    # Поле ввода почты на странице входа
    LOGIN_PAGE_EMAIL_INPUT = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input")
    # Поле ввода пароля на странице входа
    LOGIN_PAGE_PASSWORD_INPUT = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input")
    # Кнопка войти на странице входа
    LOGIN_PAGE_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти')]")
    # Кнопка регистрации на странице входа
    LOGIN_PAGE_REG_BUTTON = (By.XPATH, ".//*[contains(text(),'Зарегистрироваться')]")
    # Кнопка восстановления пароля на странице входа
    LOGIN_PAGE_RESTORE_PASSWORD_BUTTON = (By.XPATH, ".//*[contains(text(),'Восстановить пароль')]")
    # Сообщение, что пароль некорректен, на странице входа
    LOGIN_PAGE_ERROR_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

    # Заголовок страницы личного кабинета
    LK_PAGE_MAIN_LABEL = (By.XPATH, "//a[contains(text(),'Профиль')]")
    # Кнопка разлогиниться на странице личного кабинета
    LK_PAGE_LOGOUT_BUTTON = (By.XPATH, ".//*[contains(text(),'Выход')]")

    # Заголовок страницы восстановления пароля
    RESTORE_PASSWORD_PAGE_MAIN_LABEL = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    # Кнопка войти на странице восстановления пароля
    RESTORE_PASSWORD_PAGE_LOGIN_BUTTON = (By.XPATH, ".//*[contains(text(),'Войти')]")




