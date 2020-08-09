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
As specified in the docker-compose.yml file, the app uses MySQL 8.0.

```
git clone https://github.com/ncanna/Glytech
cd app
docker-compose up
```

