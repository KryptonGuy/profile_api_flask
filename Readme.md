# Profiles API

A basic REST API using Flask, Flask-RESTful, Flask-Marshmallow, and Flask-SQLAlchemy.

## Contents
---


* [Installation](#installation)
* [Models](#models)
* [Endpoints](#endpoints)

## Installation
---

```bash
make build
```

In your browser (assuming the docker-machine runs on 192.168.99.100) go to:

    http://192.168.99.100

To clean up the container mess, run
```
make clean
```

It will shut down all container and remove all images


## Models
---
### Profile

```json
{
  "name" : "Name of the profile",
  "birthdate": "Birthdate of the profile",
  "status": "ACTIVE/PAUSED"
}
```
* Default status is set tobe *"ACTIVE"*.
* Birthdate should be in format *"YYYY-MM-DD"*
* Profile id is autoincremented.

## Endpoints
---
### **API** 
>`GET` "/"
>
Gets API version and information about endpoints and methods.

### **API Documentation**
>`GET` "/doc"
>
Renders README page into html.

### **All Profiles**
>`GET` "/profile"
>
Fetch all the existing profile in the database

**Response**

*Type* `JSON`

```JSON
{
    "created_at": "timestamp",
    "data": [
        {
            "name": "name",
            "id": 1,
            "birthdate": "1978-06-20",
            "status": "ACTIVE"
        },
    ],
    "total": 1
}
```

### **Create Profile**
>`POST` "/profile"
>
Create a new profile

**Body**

*Type* `JSON`

```JSON
{
  "name": "name",
  "birthdate": "1978-06-20",
  "status": "ACTIVE"
}
```
**Response**

*Type* ``JSON``

### **ActiveProfile**
>`GET` "/profile/active"
>
Gets all the profile with status *"ACTIVE"*

**Response**

*Type* `JSON`

### **Paused Profile**
>`GET` "/profile/paused"
>
Gets all the profile with status *"PAUSED"*

**Response**

*Type* `JSON`

### **Get Profile**
>`GET` "/profile/{id}"
>
Fetch profile with given id.

**Response**

*Type* `JSON`

### **Update Profile**
>`PATCH` "/profile/{id}"
>
Update profile with given id.

**Body**

*Type* `JSON`

```JSON
{
  "name": "name",
  "birthdate": "1978-06-20",
  "status": "ACTIVE"
}
```
Send only field needed to updated.

**Response**

*Type* `JSON`

### **Delete Profile**
>`DELETE` "/profile/{id}"
>
Deletes the profile with given id.

**Response**

*Type* `JSON`