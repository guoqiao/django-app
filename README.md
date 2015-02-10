=====
django-nzpower
=====

django-nzpower is a simple Django app to provide New Zealand power companies.

Quick start
-----------

1. Add "nzpower" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'nzpower',
    ]

2. Include the URLconf in your project urls.py like this::

    url(r'^nzpower/', include('nzpower.urls')),

3. Run `python manage.py migrate` to create the models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an object (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/nzpower/
