===========
Development
===========

Contribution Guideline
======================

.. include:: ../CONTRIBUTING.rst

Issue Reporting
===============

**To Be Written**

* https://github.com/jazzband/django-redshift-backend/issues

Setup development environment
=============================

* Requires supported Python version
* do setup under django-redshift-backend.git repository root as::

    $ pip install -U pip setuptools
    $ pip install -r dev-requires.txt

Testing
=======

Run test
--------

Just run tox::

   $ tox

tox have several sections for testing.

To test the database migration as well, start postgres and test it as follows::

   $ cd tests
   $ docker-compose up -d
   $ TEST_WITH_POSTGRES=1 tox

CI (Continuous Integration)
----------------------------

All tests will be run on Github Actions:

* https://github.com/jazzband/django-redshift-backend/actions?query=workflow%3ATest


Pull Request
============

**To Be Written**

* https://github.com/jazzband/django-redshift-backend/pulls


Build package
=============

Use build::

   $ python -m build


Releasing
=========

New package version
-------------------

The django-redshift-backend package will be uploaded to PyPI: https://pypi.org/project/django-redshift-backend/.

Here is a release procefure for releasing.

.. include:: ../checklist.rst


Updated documentation
---------------------

Sphinx documentation under ``doc/`` directory on the master branch will be automatically uploaded into ReadTheDocs: https://django-redshift-backend.rtfd.io/.

