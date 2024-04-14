from selene import browser, by, command, have
import os.path


def test_form():
    browser.open('/automation-practice-form')
    # Заполнение формы
    browser.element('#firstName').type('Gandalf')
    browser.element('#lastName').type('Grey')
    browser.element('#userEmail').type('gandalf@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('March')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2024')).click()
    browser.element('.react-datepicker__day--030').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Gendolf.jpg'))
    browser.element('#currentAddress').type('adress')
    browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
    browser.element('#state').click().element(by.text('Haryana')).click()
    browser.element('#city').click().element(by.text('Karnal')).click()
    browser.element('#submit').click()

    # Проверка var1 - этот постоянно падает
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Gandalf Grey',
            'gandalf@gmail.com',
            'Male',
            '1234567890',
            '30 March,2024',
            'Arts',
            'Reading',
            'Gendolf.jpg',
            'adress',
            'Haryana Karnal'
        )
    )
    browser.element('#closeLargeModal').perform(command.js.click)
