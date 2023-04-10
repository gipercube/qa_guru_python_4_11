import allure

from automation_practice_form.model.pages.registration_page import RegistrationPage


def test_registration_form(setup_browser):
    # GIVEN
    with allure.step('Открыть главную страницу'):
        registration_page = RegistrationPage(setup_browser)
        registration_page.open()

    # WHEN
    with allure.step('Заполнить поле first name'):
        registration_page.fill_first_name('yashaka')
    with allure.step('Заполнить поле last name'):
        registration_page.fill_last_name('selene')
    with allure.step('Заполнить поле email'):
        registration_page.fill_email('yashaka@selene.com')
    with allure.step('Выбрать значение gender'):
        registration_page.select_gender('Male')
    with allure.step('Заполнить поле mobile phone'):
        registration_page.fill_mobile_phone('9876543210')
    with allure.step('Заполнить поле date of birt'):
        registration_page.fill_date_of_birth('2005', 'April', '18')
    with allure.step('Выбрать значение hobbies'):
        registration_page.select_hobbies('Reading')
    with allure.step('Заполнить поле subjects'):
        registration_page.fill_subjects('Arts')
    with allure.step('Загрузить файл в поле upload file'):
        registration_page.upload_file('/tests/resources/1.png')
    with allure.step('Заполнить поле address'):
        registration_page.fill_address('Address')
    with allure.step('ЗВыбрать значение state'):
        registration_page.select_state('NCR')
    with allure.step('Выбрать значение city'):
        registration_page.select_city('Delhi')
    with allure.step('Отправить заполненную форму'):
        registration_page.submit_click()

    # THEN
    with allure.step('Пользователь зарегистрирован. Данные верны'):
        registration_page.should_registered_user_with('yashaka selene', 'yashaka@selene.com', 'Male', '9876543210',
                                                      '18 April,2005', 'Arts', 'Reading', '1.png',
                                                      'Address', 'NCR Delhi')
