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
