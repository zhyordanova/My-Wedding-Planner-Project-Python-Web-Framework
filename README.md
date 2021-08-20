# My-Wedding-Planner-Project-Python-Web-Framework
© SoftUni Python Web Framework

 _**Welcome to MyWeddingPlanner!**_ 

This is my final exam project assignment for the course _&quot;Python Web Framework&quot;_ at SoftUni.

### Abstract

_First things first:_ Planning a wedding can feel pretty overwhelming at times. This application is designed to help the couples with the orchestration of their fairytale Wedding Day. Organization is key to keeping everything on track when you&#39;re faced with decisions, lists, deadlines, and everyday life to deal with.

### Table of Contents

### _1. Introduction_

The users have the opportunity to create their own accounts and published their favourite venues, churches, entertainment ideas, decorations, transportation companies, preferred photographers, attire and accessories etc. Each task can be like and comment from the other user


### _2. Website Overview_

Both bright and groom have access to the website.

If they are not login to their account users have the opportunity to view only the posts of registered users, and they cannot like or comment on the posts.

Registered users have the opportunity to create their own profiles and make tasklist. They cannot comment or like their own posts.

_2.1 Users_

A **Custom User Model** has been implemented to create a user object so that the email address can be used as the primary user ID instead of the authentication username.

The user objects have relational connections to all other objects in the project.

In terms of registration, users are:

  - _2.1.1 Anonymous User_

The _**anonymous user**_ has permission to view only all public post and their details. This user has restricted access to the navigation bar. He/she is able to register in the website with an email and password. Once this user has registered and logged in to the website, he/she has access to the rest of the functionality.

  - _2.1.2 Registered User_

The _**registered user**_  is already registered and can log in with an email and password. After the authentication, the user is able to navigate through the navigation bar. The registered user has his/her own profile with a first name, last name, age, phone number and image. This user has all CRUD permissions to his/her own posts. He/she can like and comment on all public posts in the system.

  - _2.1.3 Administrative User_

The _**administrative user**_ gets enabled through the admin site by the superuser. His &#39;is\_superuser&#39; and &#39;is\_staff&#39; fields are set to True. This user has all CRUD permissions over other users and their posts in the database.

_2.2 Profiles_

Every registered user has a **Profile.** The profile allows the user to reset his/her password, to update his/her own information and to delete his/her own account. The profile page shows the completion of the user&#39;s profile and his tasklist.

The **Profiles** objects have a relational connection &quot;OnetoOne&quot; with pre-created users.

  - _Profile Characteristics_

The _**Profile**_ has the following fields:

- first name - CharField with max length 30 chars
- last name - CharField with max length 30 chars
- age - PositiveIntegerField with MinValueValidator (1)
- phone\_number - CharField with validator phoneNumberRegex
- profile\_image – ImageField

_2.3 Tasklist_

The _**Tasklist**_ could be either public or private. It can be viewed by all types of users but created, edited, and deleted only by its author.

  - _2.3.1 Tasklist Characteristics_

The _**Tasklist**_ has the following fields:

- name - CharField with max length 100 chars
- quest\_capacity - PositiveIntegerField with MinValueValidator(1)
- budget - PositiveIntegerField with MinValueValidator(1)
- note - TextField
- image - ImageField
- url – URLField max length 200 chars
- category - CharField with max length 100 chars
- user - ForeignKey relation with user

  - _2.3.2 Tasklist Likes_

The _**Tasklist Like**_ could be either public or private. It can be viewed by all types of users. The author and anonymous users can&#39;t like the pub. Only the other users can like it. Once the like object is created by a single user, it can be only deleted when clicked again.

The _**Tasklist Like**_ has the following fields:

- task - ForeignKey relation with tasklist
- user - ForeignKey relation with user

  - _2.3.3 Tasklist Comments_

The _**Tasklist Comment**_ could be either public or private. It can be viewed by all types of users. The anonymous users can&#39;t comment on the  Tasklist , only the other users can.

The _**Tasklist Comment**_ has the following fields:

- comment - TextField
- task - ForeignKey relation with tasklist
- user - ForeignKey relation with user

### Technologies

- Python 3.9
- Django 3.2.6
- PostgreSQL
- Bootstrap v4
- requirements.txt file available in the project


### Setup

Project is not deployed. Please download and setup to your local environment.

### Conclusion

This project is designed for educational purposes and does not provide the full functionality of a Wedding Planner website.

###
