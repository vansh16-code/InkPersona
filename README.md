InkPersona


InkPersona is a Django-based web application designed to help writers overcome writer's block by simulating interviews with fictional characters. Writers can interact with their characters, ask them questions, and receive contextually grounded responses based on their personalities and backstories. This tool is perfect for writers who need inspiration or direction for their stories.

Table of Contents
Features

Technologies Used

Installation

Prerequisites

Clone the Repository

Set Up a Virtual Environment

Install Dependencies

Database Configuration

Create a Superuser

Usage

Contributing

License

Contact

Features
Character Interview Mode: Simulate interviews with characters based on predefined personality traits and backstories.

Customizable Character Profiles: Create characters with unique traits, backstory, fears, dreams, and secrets.

AI-Generated Responses: Utilizes Hugging Face's GPT-2 model for generating text-based answers from characters.

Responsive UI: Built with Bootstrap for a clean, mobile-friendly user interface.

Writer Assistance: Helps writers break writer's block by allowing them to ask characters questions based on their profiles.

Technologies Used
Django: High-level Python web framework for rapid development and clean design.

Hugging Face Transformers: Used for AI-powered text generation (GPT-2 model).

Bootstrap: Frontend framework for responsive and modern UI.

SQLite: Default database for storing character profiles and other data.

Python 3.8+: Programming language used to build the app.

Installation
Prerequisites
Ensure you have the following installed on your local machine:

Python 3.8 or higher

Git: For version control

Virtual Environment: Recommended to isolate dependencies

Clone the Repository
To get started, clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/InkPersona.git
cd InkPersona
Set Up a Virtual Environment
Create a virtual environment to manage project dependencies:

bash
Copy
Edit
python -m venv env
Activate the virtual environment:

Windows:

bash
Copy
Edit
.\env\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source env/bin/activate
Install Dependencies
Install the necessary dependencies listed in requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Database Configuration
Run the database migrations to set up the initial database structure:

bash
Copy
Edit
python manage.py migrate
Create a Superuser (Optional)
If you want to access the Django admin panel, create a superuser account:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to create the superuser.

Run the Development Server
Once everything is set up, start the development server:

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the app.

Usage
1. Create a Character
Navigate to the "Create Character" page.

Fill out the form with details like the character's name, personality traits, backstory, fears, and dreams.

2. Start an Interview
Once the character is created, you can start an interview.

Ask your character various questions related to their story, personality, or any other aspect you'd like to explore.

3. Receive AI-Generated Responses
Based on the defined character profile, the AI will generate contextually relevant responses to your questions.

4. Break Writer's Block
Use the interview as a creative exercise to get your writing back on track. Ask thought-provoking questions to your character and see where the conversation takes you.

Contributing
Contributions to InkPersona are welcome! To contribute, please follow these steps:

Fork the Repository: Create a fork of the repository on GitHub.

Create a New Branch: For a bug fix or feature, create a new branch.

bash
Copy
Edit
git checkout -b feature-name
Make Changes: Implement the feature or fix the bug.

Commit Changes: Write clear commit messages explaining your changes.

bash
Copy
Edit
git commit -m "Add new feature"
Push Changes: Push your changes to your fork.

bash
Copy
Edit
git push origin feature-name
Create a Pull Request: Open a pull request on the main repository with a clear description of the changes you made.

