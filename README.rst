flask-template-cookiecutter
===========================

Flask project cookiecutter template

Installation
------------

.. code:: bash

   $ mkvirtualenv blog
   $ pip install cookiecutter

Creating project template
-------------------------

.. code:: bash

   $ cookiecutter https://github.com/kuter/flask-project-cookiecutter
   full_name [user]: kuter
   project_name [Sample Flask app]: Blog
   project_slug [blog]:
   docker_pip_extra_index_ip []:
   Select open_source_license:
   1 - MIT license
   2 - BSD license
   3 - ISC license
   4 - Apache Software License 2.0
   5 - GNU General Public License v3
   6 - Not open source
   Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]: 1

Run Flask project
-----------------

.. code:: bash

   $ cd blog
   $ pip install -r requirements/dev.txt
   $ make run

Run tests
---------

.. code:: bash

   $ make test

To check against python coding standards run
--------------------------------------------

.. code:: bash

   $ make check
