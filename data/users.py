import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    user_gender: str
    user_number: str
    month: str
    year: str
    day: str
    subjects_input: str
    hobbies: str
    upload_picture: str
    current_address: str
    state: str
    city: str
