from init_db import *
from populate_db import *


def main():
    create_db_and_tables()
    create_fake_members(5)
    create_fake_coaches(7)
    create_fake_course(2)


if __name__ == "__main__":
    main()