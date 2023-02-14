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

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ python3 manage.py test
``` 
