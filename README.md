![MADE WIDTH PYTHON + DJANGO REST FRAMEWORK](http://asiani.free.fr/badges/madeWithPythonDjangoRestFramework.svg "Made with Python + Django Rest Framework")

![API REQUEST TOOL : POSTMAN](http://asiani.free.fr/badges/apiRequestToolPostman.svg "API request tool : Postman")

![DOCUMENTATION POSTMAN + MARKDOWN](http://asiani.free.fr/badges/docPostmanMarkdown.svg "Documentation Postman + Markdown")

![HELP OPENCLASSROOMS MENTOR](http://asiani.free.fr/badges/helpOpenclassroomsMento.svg "Help Openclassrooms mentor")
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# SOFTDESK - Issue Tracking System

The application to report and track technical problems for client companies in B2B.

## Technologies

- Python
- Django
- Django Rest Framework


## Contribute to the project

SOFTDESK ISSUE TRACKING SYSTEM is an open source project. Feel free to fork the source and contribute with your own features.

## Authors

The team is composed of Alain SIANI and his OpenClassRooms Mentor.

## Licensing

Free software.

## Prepare to use the API

Clone the API and launch it !

``` 
git clone https://github.com/asiani13390/softdesk.git
cd softdesk/softdesk/
python manage.py runserver
```
## Documentation

Move to the web documentation published by Postman :
[POSTMAN DOCUMENTATION](https://documenter.getpostman.com/view/26061685/2s93m8xKje)


## Howto

Use the POSTMAN request API application

Use endpoint to register the API

Use enpoint to login the API


| # | API Endpoint | HTTP Method | URI  |
|--:|---------|:--:|:----|
|1|  User registration  | POST  | /signup/ |
|2|  User's login       | POST  | /login/ |
|3|  Retrieve the list of all the projects attached to the connected user | GET  | /projects/ |
|4|  Create a project | POST   | /projects/ |
|5|  Retrieve project details from its id | GET    | /projects/{id}/ |
|6|  Update a project | PUT    | /projects/{id}/ |
|7|  Delete a project and its problems | DELETE | /projects/{id}/ |
|8|  Add a collaborator to a project | POST   | /projects/{id}/users/ |
|9|  Retrieve the list of all users attached to a project | GET    | /projects/{id}/users/ |
|10| Remove a user from a project | DELETE  | /projects/{id}/users/{id} |
|11| Retrieve the list of problems related to a project | GET    | /projects/{id}/issues/ |
|12| Creating a problem in a project | POST   | /projects/{id}/issues/  |
|13| Update a problem in a project | PUT    | /projects/{id}/issues/{id}  |
|14| Delete a problem from a project | DELETE | /projects/{id}/issues/{id} |
|15| Create comments on a problem | POST   | /projects/{id}/issues/{id}/comments/ |
|16| Retrieve the list of all comments related to a problem| GET    | /projects/{id}/issues/{id}/comments/ |
|17| Edit a comment | PUT    | /projects/{id}/issues/{id}/comments/{id} |
|18| Delete a comment | DELETE | /projects/{id}/issues/{id}/comments/{id} |
|19| Get a comment via its id | GET    | /projects/{id}/issues/{id}/comments/{id} |


**Endpoints**

```
The base URL will be : "http://localhost:8000/admin/issue_tracking_system"

You must be authenticated to use endpoints.
```

3. Retrieve the list of all the projects attached to the user connected 

    
    * Open Postman
    * Use method "GET"
    * URI : /projects/ 
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button
 
    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Project is available only for its author or its contributor|

    |RESULT|
    |------|
    |Result : A JSON table of projects where the user connected is a contributor or author.|
    

4. Create a project

    * Open Postman
    * Use method "POST"
    * URI : /projects/
    * Headers : Authorization = Bearer [access token]
    * Body : Raw - JSON 

        ```{ "title": "Deep security deployment", "description": "Protect all computers", "type": "Improvement", "author": "1" }```
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    
    |RESULT|
    |------|
    |Result : A JSON table of projects where the user connected is a contributor or author.|

5. Retrieve project details from its id

    * Open Postman
    * Use method "GET"
    * URI : /projects/{id}/
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Project is available only for its author or its contributor|
    
    |RESULT|
    |------|
    |Result : A JSON table of the project|

6. Update a project

    * Open Postman
    * Use method "PUT"
    * URI : /projects/{id}/
    * Headers : Authorization = Bearer [access token]
    * Body : 
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Update a project is only available for its author|
    
    |RESULT|
    |------|
    |Not authenticated : Given token not valid for any token type|
    |Is author : A JSON table of the project update|
    |Is contributor but not author : You do not have permission to perform this action.|

7. Delete a project and its problems 

    * Open Postman
    * Use method "DELETE"
    * URI : /projects/{id}/
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Delete a project is only available for its author|
    
    |RESULT|
    |------|
    |Not authenticated : Given token not valid for any token type|
    |Is author : Empty result|
    |Is contributor but not author : You do not have permission to perform this action.|

8. Add a collaborator to a project

    * Open Postman
    * Use method "POST"
    * URI : /projects/{id}/users/
    * Headers : Authorization = Bearer [access token]
    * Body : Raw - JSON
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Add a contributor is only available for the project author|
    
    |RESULT|
    |------|
    |Not authenticated : Given token not valid for any token type|
    |Is author : JSON table of user inserted|
    |Is not the project author : You do not have permission to perform this action.|

9. Retrieve the list of all users attached to a project

    * Open Postman
    * Use method "GET"
    * URI : /projects/{id}/users/
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |List contributors is available for the project author and contributors|
    
    |RESULT|
    |------|
    |Not authenticated : Given token not valid for any token type|
    |Authenticated only : You do not have permission to perform this action.|
    |Is author or contributor : JSON table of project's contributors|

10. Remove a user from a project | DELETE  | /projects/{id}/users/{id}

    * Open Postman
    * Use method "DELETE"
    * URI : /projects/{id}/users/{id}
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Delete a contributor is available only to the project author|
    
    |RESULT|
    |------|
    |Not authenticated : Given token not valid for any token type|
    |Authenticated only : You do not have permission to perform this action.|
    |Is author : JSON table of project's contributors|


