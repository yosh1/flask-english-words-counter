# Flask English words counter
This is Flask application that is able to count words and sentences.

---

## How to run?

### Local

```
$ pip install flask
$ python3 app.py
```

### Docker

```
$ docker build -t flask_count_app .
# Make docker image

$ docker run -p 5000:5000 -it flask_count_app
# Start container and expose 5000 port

$ docker run -p 5000:5000 -it flask_count_app /bin/bash
# into container (bash)
```
