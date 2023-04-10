import os
from selene import have, command


class RegistrationPage:
    def __init__(self, setup_browser):
        self.browser = setup_browser
        self.first_name = self.browser.element('#firstName')
        self.last_name = self.browser.element('#lastName')
        self.email = self.browser.element('#userEmail')
        self.gender = self.browser.element('[for="gender-radio-1"]')
        self.user_number = self.browser.element('#userNumber')
        self.date_of_birth_input = self.browser.element('#dateOfBirthInput')
        self.date_of_birth_year = self.browser.element('.react-datepicker__year-select')
        self.date_of_birth_month = self.browser.element('.react-datepicker__month-select')
        self.subjects_input = self.browser.element('#subjectsInput')
        self.hobbies = self.browser.element('[for="hobbies-checkbox-2"]')
        self.upload_picture = self.browser.element('#uploadPicture')
        self.address = self.browser.element('#currentAddress')
        self.state = self.browser.element('#state')
        self.state_select = self.browser.element('#react-select-3-option-0')
        self.city = self.browser.element('#city')
        self.city_select = self.browser.element('#react-select-4-option-0')
        self.submit = self.browser.element('#submit')

    def open(self):
        self.browser.open('http://demoqa.com/automation-practice-form')
        self.browser.config.driver.maximize_window()
        self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self, value):
        self.gender.should(have.text(f'{value}')).click()
        return self

    def fill_mobile_phone(self, value):
        self.user_number.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(month)
        self.date_of_birth_year.type(year)
        self.browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def select_hobbies(self, value):
        self.hobbies.should(have.text(value)).click()
        return self

    def fill_subjects(self, value):
        self.subjects_input.type(f'{value}').press_enter()
        return self

    def upload_file(self, value):
        self.upload_picture.send_keys(os.getcwd() + value)
        return self

    def fill_address(self, value):
        self.address.type(value)

    def select_state(self, value):
        self.state.click()
        self.state_select.should(have.text(f'{value}')).click()
        return self

    def select_city(self, value):
        self.city.click()
        self.city_select.should(have.text(f'{value}')).click()
        return self

    def submit_click(self):
        self.submit.click()
        return self

    def should_registered_user_with(self, full_name, email, gender, number, dateofbirth, subjects, hobbies, photo,
                                    address, stateandcity):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                dateofbirth,
                subjects,
                hobbies,
                photo,
                address,
                stateandcity,
            )
        )
        return self
