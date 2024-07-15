Indostan Builders
Overview
Indostan Builders is a static website created for a renowned construction company. The website is designed to showcase their projects, values, vision, and the cities they serve. As the sole developer, I was responsible for the complete development and deployment of the site. The website was successfully hosted on an AWS EC2 instance, demonstrating my ability to manage both the development and deployment processes independently.

Features
Home Page: Overview of the company and its mission.
Projects Page: Detailed showcase of completed and ongoing projects.
About Us Page: Information about the company's values, vision, and history.
Contact Page: Contact information and a contact form for inquiries.
Service Areas Page: Cities and regions where the company operates.
Tech Stack
Backend Framework: Django
Hosting: AWS EC2
Installation and Setup
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd indostan-builders
Create and Activate a Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Website:
Open your web browser and navigate to http://127.0.0.1:8000.

Deployment
The website is hosted on an AWS EC2 instance. Follow these steps to deploy the Django application:

Set up an EC2 Instance:

Launch an EC2 instance using the AWS Management Console.
Choose an Amazon Machine Image (AMI) and instance type.
Configure security groups to allow HTTP and SSH access.
SSH into the Instance:

bash
Copy code
ssh -i /path/to/your-key.pem ec2-user@your-ec2-public-ip
Install Dependencies on the EC2 Instance:

bash
Copy code
sudo yum update -y
sudo yum install python3 python3-venv -y
Transfer Project Files:

Use scp or another method to transfer your project files to the EC2 instance.
Set up the Project on the EC2 Instance:

bash
Copy code
cd /path/to/project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
Run the Django Application:

bash
Copy code
python manage.py runserver 0.0.0.0:8000
Configure Nginx and Gunicorn:

Set up Nginx as a reverse proxy.
Use Gunicorn to serve the Django application.
Contact
For any inquiries or support, please contact:

Email: support@indostanbuilders.com
