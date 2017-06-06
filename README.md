## MyNotes
restful API Simple note using Django Rest Framework.

### Dependencies
Just typing:

```
pip install -r requirements.txt
```

### Prepare
I recommend to use Python3 and do not forget to enable your virtual env.

```
python manage.py makemigrations notes
python manage.py migrate 
```

Remember to create superuser:

```
python manage.py createsuperuser
```

### Endpoint API
There are four endpoints you can use:

* `/users/`: using `GET` and read-only for get all users.
* `/users/username/`: using `GET` and read-only for retrieve user from username given.
* `/notes/`: using `GET` to get all notes (using Basic Authorization in your request header).
* `/notes/`: using `POST` to create new note (using Basic Authorization in your request header).
* `/notes/pk/`: using `GET` to retrieve user from `pk`. `pk` is a unique id  (using Basic Authorization in your request header).
* `/notes/pk/`: using `PUT` to update user from `pk` (using Basic Authorization in your request header).
* `/notes/pk/`: using `DELETE` to remove user from `pk` (using Basic Authorization in your request header).
* `/notes/?title=yourtitle&username=yourusername`: using `GET` to get all notes using query params (using Basic Authorization in your request header).

Remember to set request header using Basic Authorization. Here, I do not use token or OAuth token. You can develop it for learning purposes.