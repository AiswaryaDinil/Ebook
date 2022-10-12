## _Django-Ecommerce-Book_
<p>An online bookstore web API implementing basic online store functionalities.:) </p>

 ### Stack
- Python
- Django
- SQLite
- VS Code

### Requirements
* Django 
* Pypi packages
* Database:SQLite

<p>Lets begin our project by starting our project and installing a bookapo app, type below commands in terminal. </p>

(django_project)$`django-admin startproject Ebook .`
(django_project)$`python manage.py startapp bookapi`
Now, open your favourite IDE and locate this project directory. (Im using VS Code) note that at this point django doesnt know about this app, therefore we need to mention this app name inside our settings.py file.
### models
When done with the settings.py file, open the Ebook folder, in here you we find models.py file with fields: title,author,genre,review,favourite
### migrations 
now its time to create some tables in our database, most of which is already handled by django, we just need to run following commands:
(django_project)$`python manage.py makemigrations`
(django_project)$`python manage.py migrate`
### server
Now, lets check that our model is being registered properly or not. First lets ensure that our server is running properly. Put the following commmand in terminal:
(django_project)$`python manage.py runserver`
* now open this link in your browser http://127.0.0.1:8000/
### views
Now we need to work on views. In this case im gonna use 'Class Based Views'.The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes.
The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().
* we only need to provide at least the queryset and serializer_class attributes.
* By using routers, we no longer need to deal with wiring up the URL conf ourselves.
* The 'BookView' is a class which basically using the django module ModelViewset to CRUD operations on one or many ebooks. The API should also be able to
return ebook lists that sorted and/or filtered ebooks by any of the fields.

### urls
Now to make our class based views work we need url routing. By default we have a single urls.py file in our Ebook directory and not in bookapi app.


### API Actions:

* Create the book with title,author,genre,review,favourite
* Retrieve books details by the ID
* Update books and their fields
* Delete the added books
* retrieve a list of books associate with an author,genre,title

## ScreenShots
![](https://github.com/AiswaryaDinil/Ebook/blob/master/images/Screenshot%201.png)
![](https://github.com/AiswaryaDinil/Ebook/blob/master/images/Screenshot%202.png)
![](https://github.com/AiswaryaDinil/Ebook/blob/master/images/Screenshot%203.png)
![](https://github.com/AiswaryaDinil/Ebook/blob/master/images/Screenshot%204.png)
![](https://github.com/AiswaryaDinil/Ebook/blob/master/images/Screenshot%205.png)
