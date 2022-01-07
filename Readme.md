#Introduction

This Flasked Based API used to manage Profiles.

**Get All Profiles**
----
  Fetch all the profiles int database

* **URL**

  '/profiles'

* **Method:**

  '''http
    GET /profile
  '''
  
* **Success Response:**


* **Code:** 200 <br />

**Create Profile**
----
  Create new profile in database

* **URL**

  '/profiles'

* **Method:**

  '''http
    POST /profile
  '''

* **Data Params**

''' {
    "name": "name",
    "birthdate": "birthdate",
    "status": "status",
}  
  '''

birthdate should be in format 'YYYY-MM-DD'


* **Success Response:**
    

* **Code:** 200 <br />

