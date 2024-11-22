
<p align="center">SQLmodel_Streamlit</p>

# <p align="center">La Poigne d'Acier</p>
<p align="center">
    <img src="images/banner.png" alt="Banner">
</p>

This project is a web application designed to modernize the management of "La Poigne d’Acier," a gym offering a variety of fitness classes. The app aims to streamline administrative tasks for staff and improve the user experience for gym members.

## ➤ Menu

* [➤ Project Structure](#-project-structure)
* [➤ How to Run](#-how-to-run)
* [➤ Requirements](#-requirements)
* [➤ Outputs](#-outputs)
* [➤ Evaluation Criteria](#-evaluation-criteria)
* [➤ Performance Metrics](#-performance-metrics)
* [➤ License](#-license)
* [➤ Author](#-author)

---

## Project Structure

- `models.py`: Defines SQLModel models for database tables.
- `init_db.py`: Script to initialize the SQLite database and create tables.
- `populate_db.py`: Generates and populates the database with mock data.
- `Home page.py`: Streamlit_based Home page interface.
- `pages`:
    - `Membre.py`: Streamlit-based user interface for gym members.
    - `Admin.py`: Streamlit-based admin interface for staff.
- `poigne_database.db`: SQLite database file.
- `requirements.txt`: List of required Python dependencies.
- `images`:
    - `banner.png`: Image for the app.

---

## How to Run

1. Ensure Python is installed on your system.
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/gvannesson/Simplon_SQLmodel_Streamlit.git
   ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the main script to start the application:
    ```bash 
    python main.py
    ```
    ```bash
    streamlit run Home\ page.py

# Requirements

- Python 3.8+
- SQLite: For database management.
- Streamlit: For creating interactive web applications.
- SQLModel: An ORM for database handling.
- Faker: For generating mock data.

## ERD Diagram
<p align="center">
    <img src="images/ERD diagram.png" alt="ERD">
</p>


## Outputs

### Member Interface:
- Register for classes (with seat availability and schedule conflict checks).
- Cancel class registrations.
- View registration history.
### Admin Interface:
- Manage coaches (add, update, delete).
- Manage classes (add, update, cancel).
- View registration history for each member.
- Cancel registrations.

# Evaluation Criteria

- Database Design: Accurate modeling of entities and relationships using SQLModel.
- Functionality: Full implementation of all member and admin features.
Code Organization: Clean and modular code structure.
User Interface: Simple and intuitive Streamlit-based UI.
Data Integrity: Validation for schedule conflicts and class capacity.

## Performance Metrics

- Functional Requirements: All mandatory functionalities are implemented and working.
- User Interface: Intuitive and user-friendly design.
- Code Quality:
    - Structured and modular code.
    - Comprehensive documentation (docstrings and comments).
- Bonus: Additional features that are well-integrated.

## License
MIT License

Copyright (c) 2024 Gautier Vanesson & Khadija Aassi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author

Gauthier Vannesson  <a href="https://github.com/gvannesson" target="_blank"> <img loading="lazy" src="images/github-mark.png" width="30" height="30" style="vertical-align: middle; margin-left: 15px;" alt="GitHub Logo"> </a>


Khadija Aassi <a href="https://github.com/Khadaassi" target="_blank"> <img loading="lazy" src="images/github-mark.png" width="30" height="30" style="vertical-align: middle; margin-left: 15px;" alt="GitHub Logo"> </a>

