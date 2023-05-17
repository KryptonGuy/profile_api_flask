# Employee Profile Management REST API
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Managing employee profiles can be a complex task that requires a streamlined and efficient system. With this REST API, we aim to simplify the process of managing employee profiles by providing a comprehensive and user-friendly solution.

## Features

This REST API offers the following features:

- Create, read, update, and delete employee profiles
- Retrieve a list of all employee profiles or search for specific profiles based on criteria such as name, department, or job title
- Store employee profiles in a database for easy retrieval and management
- Validate and sanitize input data to ensure data integrity and consistency
- Authenticate and authorize users with appropriate access levels

## Technologies Used

This project was built using the following technologies:

- Python
- Flask
- Flask-RESTful
- Flask-Marshmallow
- Flask-SQLAlchemy
- SQLite (or your preferred database management system)
## Installation

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


For detailed information on how to use each endpoint, refer to the API documentation or the Swagger UI (available at `/swagger`) when running the API locally.


## Contributing

We welcome contributions from the community. If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.
