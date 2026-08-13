from faker import Faker

fake = Faker()


def generate_users(count):
    users = []
    for _ in range(count):
        users.append(
            {
                "name": fake.name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "address": fake.address(),
                "dob": str(fake.date_of_birth(minimum_age=18)),
            }
        )
    return users


fakerdata = generate_users(5)
for user in fakerdata:
    print(user)
