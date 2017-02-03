# Udacity-Item-catalog-Project
RestaurantMenu App for Item catalog project
This is a python module that creates a website and JSON API for a list of restaurants. Each restaurant displays their menus and also provides user authentication using Google.
Registered users will have ability to edit and delete their own items. This application uses Flask,SQL Alchemy, JQuery,CSS, Javascript, and OAuth2 to create Item catalog website.

Installation
1.virtualBox
2.Vagrant
3.python 2.7

Instructions to Run the project

Setting up OAuth 2.0
1. You will need to signup for a google account and set up a client id and secret.
2. Visit http://console.developers.google.com for google setup.

Setting up the Environment

1. clone or download the repo into vagrant environment.
2. Type command vagrant up,vagrant ssh.
3. In VM, cd /vagrant/catalog
4. Run python database_setup.py to create the database.
5. Run Python lotsofmenus.py to add the menu items
6. Run python 'project.py'
7. open your webbrowser and visit http://localhost:8000/ 

References
http://discussions.udacity.com/



