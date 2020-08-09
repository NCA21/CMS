# Summary
This project aimed to build a glucose management software for insulin therapy candidates and patients, similar to systems employed in healthcare settings as well as electronic health record software.

```
./app
│
└───cms
│    └───cms
│        │   settings.py
│        │   urls.py
│        │   wsgi.py
│    └───records
│        │   __init__.py
│        │   admin.py
│        │   apps.py
│        │   models.py
│        │   tests.py
│        │   urls.py
│        │   views.py
│        └───migrations
│            │   ...
│        └───templates
│            └───records
│                └───css
│                    │   ...
│                │   base.html
│                │   index.html
│   │   db.json
│   │   manage.py
│
```

# Usage
The services that make up the app are defined in ```docker-compose.yml```. To run the app, firstly clone the repoository, change directory to the app, and run ```docker-compose up```.

```
git clone https://github.com/ncanna/Glytech
cd app
docker-compose up
```

