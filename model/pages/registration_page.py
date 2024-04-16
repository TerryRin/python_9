import os

from selene import command, have, by
from selene.support.shared import browser


class RegistationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects_input = browser.element('#subjectsInput')
        self.up_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')
        self.close_large_modal = browser.element('#closeLargeModal')

    def user_registration(self, user):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.user_email.type(user.email)
        browser.element(by.text(user.gender)).perform(command.js.click)
        self.user_number.type(user.number)
        self.date_of_birth.click()
        browser.element('.react-datepicker__month-select').type(user.month).click()
        browser.element('.react-datepicker__year-select').click().type(user.year).click()
        browser.element(f'.react-datepicker__day--0{user.day}').click()
        self.subjects_input.type(user.subjects_input).press_enter()
        browser.element(by.text(user.hobbies)).perform(command.js.click)
        self.up_picture.send_keys(os.path.abspath(f'resources/{user.upload_picture}'))
        self.current_address.type(user.current_address)
        self.current_address.perform(command.js.scroll_into_view)
        self.state.click()
        browser.element(by.text(user.state)).perform(command.js.click)
        self.city.click()
        browser.element(by.text(user.city)).perform(command.js.click)
        self.submit.click()

    def open(self):
        browser.open('/automation-practice-form')
        return self
    def should_finish_form_title(self, value):
        browser.element('.modal-title').should(have.text(value))

    def should_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.number,
                f'{user.day} {user.month},{user.year}',
                user.subjects_input,
                user.hobbies,
                user.upload_picture,
                user.current_address,
                f'{user.state} {user.city}'
            )
        )

    def close_large_modal(self):
        self.close_large_modal.perform(command.js.click)
