# Banks Applications

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/arturoverbel/interview_banks
$ cd interview_banks
```
Then install the dependencies:

```sh
$ pip3 install -r requirements.txt
```
Once `pip3` has finished downloading the dependencies:
```sh
$ python3 manage.py runserver
```
And navigate to `http://127.0.0.1:8000/gocardless/`.

### Directory

    .
    ├── accounts                # Module for users (login, signup)
    ├── bank                    # Mainly app. Manage the Bank and Provider modules
    │   ├── migrations          # Migrations for Bank and Providers
    │   ├── router              # Manage all router,include the router render
    │   ├── views               # Represent the controller of the app.
    │   ├── models.py           # Bank and Providers Models
    └── README.md

## Docker

To build a image. Run:
```sh
$ docker build . -t app_banks_v0.0
``` 

To Run:
```sh
docker run app_banks_v0.0
```

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ python3 manage.py test
``` 
