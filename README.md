# JWT Sample project

This project is only for testing purposes. Its main goal is to see how the
JSON Web Token authentication work in combination with `django-rest-framework`
library, and using `djangorestframework-jwt` package.

Once you have some users in the database, you should be able to call the 
`/api-token-auth/` endpoint with valid `username` and `password` to get a
JWT (JSON web token). Use the JWT later on to authenticate all your requests.


#### Let's create a testing user
```python
In [1]: from django.contrib.auth.models import User

In [2]: user = User(username='johndoe', email='john@doe.com')

In [3]: user.set_password('FooBar123!')

In [4]: user.save()
```


#### Request restricted endpoint without a valid JWT
```bash
$ curl http://localhost:8000/restricted/

{
    "detail": "Authentication credentials were not provided."
}
```


#### Obtain a JWT
```bash
$ curl
    -X POST
    -H "Content-Type: application/json"
    -d '{"username": "johndoe", "password": "FooBar123!"}'
    http://localhost:8000/api-token-auth/

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5AZG9lLmNvbSIsInVzZXJuYW1lIjoiam9obmRvZSIsImV4cCI6MTQ2ODkyNTM5OSwidXNlcl9pZCI6MX0._rY5qiO6KLPwBgjIdyRYYiSQhWvGwaOCwHeIN2ErZos"
}
```

#### Request restricted endpoint providing a valid JWT
```bash
$ curl
    -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5AZG9lLmNvbSIsInVzZXJuYW1lIjoiam9obmRvZSIsImV4cCI6MTQ2ODkyNTM5OSwidXNlcl9pZCI6MX0._rY5qiO6KLPwBgjIdyRYYiSQhWvGwaOCwHeIN2ErZos"
    http://localhost:8000/restricted/

{
    "id": 1,
    "username": "johndoe"
}
```
