# CA2_Thoughts_24059
## Continuous Assessment 2 - Back End - Django

On this Assessment I have been requested to create a web application using the Django framework,
and use the main functionalities in the database (CRUD: Create, Read, Update, and Delete), so I created an application where users can sign up, and then add simple thoughts to be shared in the index page (Home page), after adding thoughts the user can also delete or update their thoughts in the “My Thoughts” page.
### CRUD
1.Create: add thoughts.\
2.Read: get thoughts from the database and display it on the web page.\
3.Update: edit thoughts (Text).\
4.Delete: remove thoughts from the database.\

### To run this application on your PC:

1.Clone the repository from GitHub: \
`git clone https://github.com/sbritobreno/DjangoFirstProject.git`, somewhere
in your computer.\
2. Change a few settings on the database (`djangoproject/settings.py line 76`), adding your own settings and also creating a database
in MySQL with workbench or command line (query = `CREATE DATABASE thoughts`), make sure to name it thoughts or change the name in the settings as well,
also, before running the program, you have to run the command `py manage.py createsuperuser 
in order` to create a user to use the program as an Admin and also run the command
`py manage.py makemigrations` and `py manage.py migrate` to load the changes from the database settings, after that you can run the command 
`py manage.py runserver` to finally run the program, then you can go to your browser
and access the `localhost:8000/` URL.

# CA3_Thoughts_24059
## Continuous Assessment 2 - Back End - Django Test and Security

On this assignment I have been testing a few parts of the application I built while doing the last assessment(CA2). First of all I have not made any changes on the application itself but I did deleted all the test.py files on the application as one of the requirements was to create an external folder with all the test files in it, so I created a folder called 'tests' on the project directory, and inside it I created a test file for models (test_models.py), where I implemented 2 tests one for creating a new 'thought', including a function setUp that creates an user, which will be the user that creates the 'thought', and another test that returns the 'thought' as a string that would be then loaded to the view, and on this test I forced and error, which is display on the command line when running the tests. I have also created another 2 tests for Views on the file test_views.py, one of the test return all the thoughts that is display on the home page, and the other one returns only the 'thoughts' that was created by the current user, I have implemented all test using TestCase from django.test, and apart from those two test files I have also created a test_settings.py file where I set again all the application settings but now with a few small changes such as on the INSTALLED_APPS where I added the test, and  I have also modified the database settings in order to create another database so I would not inject any fake data to the app's database. As another requirement I have also created a small script with a configuration to run all the test in a different enviroment.

### Command to run the config script and tests:
python run_tests.py
