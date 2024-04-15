from data.users import User
from model.pages.registration_page import RegistationPage


def test_form():
    test_user = User(
        first_name='Gandalf',
        last_name='Grey',
        email='gandalf@gmail.com',
        user_gender='Male',
        user_number='1234567890',
        month='March',
        year='2024',
        day='30',
        subjects_input='Arts',
        hobbies='Reading',
        upload_picture='Gendolf.jpg',
        current_address='adress',
        state='Haryana',
        city='Karnal'
    )

    registation_page = RegistationPage()
    registation_page.open()
    registation_page.user_registration(test_user)
    registation_page.should_finish_form_title('Thanks for submitting the form')
    registation_page.should_registered_user_with(test_user)
    registation_page.close_large_modal()
