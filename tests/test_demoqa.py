from data.users import User
from model.pages.registration_page import RegistrationPage


def test_form():
    test_user = User(
        first_name='Gandalf',
        last_name='Grey',
        email='gandalf@gmail.com',
        gender='Male',
        number='1234567890',
        month='March',
        year='2024',
        day='30',
        subjects_input='Arts',
        hobbies='Reading',
        upload_picture='Gendolf.jpg',
        current_address='address',
        state='Haryana',
        city='Karnal'
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.user_registration(test_user)
    registration_page.should_registered_user_with(test_user)
    registration_page.close_large_modal()
