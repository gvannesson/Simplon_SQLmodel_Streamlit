from init_db import *
from populate_db import *


def main():
    create_db_and_tables()
    create_fake_members(10)
    create_fake_coaches(7)
    create_fake_courses(20)
    create_fake_registrations(30)

if __name__ == "__main__":
    main()
