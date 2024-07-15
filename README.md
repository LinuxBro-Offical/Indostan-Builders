# Indostan Builders

**Overview:**
Indostan Builders is a static website created for a renowned construction company. The website is designed to showcase their projects, values, vision, and the cities they serve. As the sole developer, I was responsible for the complete development and deployment of the site. The website was successfully hosted on an AWS EC2 instance, demonstrating my ability to manage both the development and deployment processes independently.

**Features:**
Home Page: Overview of the company and its mission.
Projects Page: Detailed showcase of completed and ongoing projects.
About Us Page: Information about the company's values, vision, and history.
Contact Page: Contact information and a contact form for inquiries.
Service Areas Page: Cities and regions where the company operates.

**Tech Stack:**
Backend Framework: Django
Hosting: AWS EC2
Installation and Setup
Clone the Repository:

git clone <repository-url>
cd indostan-builders

Create and Activate a Virtual Environment:
python3 -m venv venv
source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Run Migrations:
python manage.py migrate
Run the Development Server:

python manage.py runserver

Access the Website:
Open your web browser and navigate to **http://127.0.0.1:8000.**
