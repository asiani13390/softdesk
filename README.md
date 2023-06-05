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

This programm has been tested with **python 3.9.13**

Get source of programm : Clone the API 

``` 
git clone https://github.com/asiani13390/softdesk.git
```

Move into the project

``` 
cd softdesk
``` 

Create python virtual environement

``` 
python -m venv env
``` 

Activate the python virtual environment

``` 
source ./env/bin/activate
``` 

Import modules

``` 
pip install -r requirements.txt
``` 

Run django server

```
cd softdesk/
python manage.py runserver
```

## Softdesk Postman documentation

Link for Postman published documentation  :
[POSTMAN DOCUMENTATION](https://documenter.getpostman.com/view/26061685/2s93m8xKje)

## Postman installation

Download Postman from : `https://www.postman.com/`

### Example for Linux (x64)

* Open your navigator : `https://www.postman.com/`
* Select 'Download the desktop app for Linux'
* Clic "Linux (x64)"
* Postman is downloaded
* Move the application where you want
* Decompresser l'archive
```
tar xvzf postman-linux-x64.tar.gz
```
* Move into Postman folder
```
cd Postman
```
* Run Postman application
```
./Postman
```

## Import Postman published documentation

* Open your browser to the published postman documentation :
`https://documenter.getpostman.com/view/26061685/2s93m8xKje`

* Click "Run in Postman" button on the top right
* Select the local postman application
* Select workplace to import the collection
* Click "Import"
* Click on "Collections"

Now, you can show the collection in local Postman application.

## Howto

### General

* Open Postman request API application
* Use endpoint to register the API
* Use endpoint to login the API
* Use endpoints...

### API Details

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

You must be registered and authenticated to use endpoints.
```
1. User signup (Register)

    **Access**
    Endpoint is limited to : 

    |PERMISSIONS  |
    |-------------|
    |AllowAny     |

    **Run query**
    * Open Postman
    * Use method "POST"
    * URI : /signup/
    * Headers : Nothing
    * Body : Raw - JSON 
    
        ```
        {
             "first_name": "Laurent",
             "last_name": "Dupont",
             "email": "ldupont@softdesk.fr",
             "username": "ldupont",
             "password": "xxx"
        }
        ```
   * Click "Send" button
   * Postman launch the query 
   * Postman show result and serializer data 
        * Result : "Status: 201 Created"

            ```
            {
                "first_name": "Didier",
                "last_name": "Dupont",
                "username": "ddupont",
                "email": "ddupont@softdesk.fr",
                "date_joined": "2023-06-05T08:03:14.395287Z"
            }
            ```

    |RULES|
    |-----|
    |Allow anyone to register|


2. User login

    **Access**
    Endpoint is limited to : 

    |PERMISSIONS  |
    |-------------|
    |AllowAny     |

    **Run query**
    * Open Postman
    * Use method "POST"
    * URI : /login/
    * Headers : Nothing
    * Body : Raw - JSON 
    
        ```
        {
        	"username": "ddupont",
        	"password": "xxxx"
	    }
        ```
   * Click "Send" button
   * Postman launch the query 
   * Postman show result and serializer data 
   * Result : "Status: 200 OK"
        ```
        {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NjA0MDE4OCwianRpIjoiOTU1NjZjYTQ3NDg4NDZkZjhmZGI4MjE1ZjVjNzViNGEiLCJ1c2VyX2lkIjoxNn0.5lnlmch_FI46LDasZyhTrXwyUO7s48_CPi49VWOqc8Q",
		
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4NTQ1Nzg4LCJqdGkiOiIxZjI1ODg0ZGE3YTU0OTdhYTI0NDhhNjNiYzlhODk0MSIsInVzZXJfaWQiOjE2fQ.DhnBFoxt5InRcWMJzKaMz4X-RrSFh8KL-fZGi-lyLno"
		}
        ```

    |RULES|
    |-----|
    |Allow anyone to login|


3. Retrieve the list of all the projects attached to the connected user

    **Access**
    Endpoint is limited to : 

    |PERMISSIONS|
    |-----------|
    |IsAuthenticated|
    |PermissionProject|
	
    **Run query**
    * Open Postman
    * Use method "GET"
    * URI : /projects/
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button
    * Postman launch the query 
    * Postman show result and serializer data 
    * Result : "Status: 200 OK"
        ```
        {
            "id": 32,
        	"title": "ASI_PROJECT_01",
        	"description": "Description du projet ASI_01",
        	"type": "backend",
        	"author": 1,
        	"contributors": []
    	}
        ```
        
    |RULES|
    |------|
    |User must be authenticated|
    |A project is only accessible to its manager and contributors|


4. Create a project

    **Access**
    Endpoint is limited to : 

    |PERMISSIONS|
    |-----------|
    |IsAuthenticated|
    |PermissionProject|
	
    **Run query**
    * Open Postman
    * Use method "POST"
    * URI : /projects/
    * Headers : Authorization = Bearer [access token]
    * Body : Raw - JSON 
    
    ```
        { 
            "title": "PROJECT_ASI_02",
            "description": "Project description for ASI Project 02",
            "type": "IOS",
            "author": "1" 
        }
    ```
    * Click "Send" button
    * Postman launch the query 
    * Postman show result and serializer data 
    * Result : "Status: 201 OK"
        ```
            {
                "id": 33,
                "title": "PROJECT_ASI_02",
                "description": "Project description for ASI Project 02.",
                "type": "IOS",
                "author": 1,
                "contributors": []
            }
        ```
        
    |RULES|
    |------|
    |User must be authenticated|
    |Authenticated user can create a project|


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

10. Remove a user from a project

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


11. Retrieve the list of problems related to a project

    * Open Postman
    * Use method "GET"
    * URI : /projects/{id}/issues/
    * Headers : Authorization = Bearer [access token]
    * Body : None
    * Click "Send" button

    |PERMISSIONS|
    |-----------|
    |Authenticated user|
    |Only contributors are able to create and read project's issues|
    

    |RESULT|
    |------|
    |Not authenticated : Given token not valid for any token type|
    |Authenticated only : You do not have permission to perform this action.|
    |Is contributor : JSON table of project's issues|
