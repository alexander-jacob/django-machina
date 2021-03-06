django-machina
##############

.. image:: https://readthedocs.org/projects/django-machina/badge/?style=flat-square&version=stable
   :target: http://django-machina.readthedocs.org/en/stable/
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/l/django-machina.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-machina/
    :alt: License

.. image:: http://img.shields.io/pypi/v/django-machina.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-machina/
    :alt: Latest Version

.. image:: https://img.shields.io/gitter/room/ellmetha/django-machina.svg?maxAge=2592000&style=flat-square
   :target: https://gitter.im/ellmetha/django-machina
   :alt: Join chat

.. image:: http://img.shields.io/travis/ellmetha/django-machina.svg?style=flat-square
    :target: http://travis-ci.org/ellmetha/django-machina
    :alt: Build status

.. image:: https://img.shields.io/codecov/c/github/ellmetha/django-machina.svg?style=flat-square
    :target: https://codecov.io/github/ellmetha/django-machina
    :alt: Codecov status

|

*Django-machina* is a forum framework for Django providing a way to build community-driven websites. It offers a full-featured yet very extensible forum solution:

* Topic and post editing
* Forums tree management
* Per-forum permissions
* Anonymous posting
* Polls and attachments
* Moderation and pre-moderation
* Forum conversations search
* ...

.. image:: https://raw.githubusercontent.com/ellmetha/django-machina/master/docs/_images/machina_forum_header.png
  :target: http://django-machina.readthedocs.org/

|

*Django-machina* was built with integration in mind: the application is designed to be used inside existing Django applications. It is not a standalone forum solution.

*Django-machina* was built with customization and extensibility in mind: each single functionality of the application can be customized or overriden to accommodate with your needs. In fact, *django-machina* uses the same techniques as those introduced by the famous django-oscar_ e-commerce framework to allow powerfull customizations.

.. _django-oscar: https://github.com/django-oscar/django-oscar

.. contents:: :local:

Documentation
=============

Online browsable documentation is available at https://django-machina.readthedocs.org.

Head over to the documentation for all the details on how to set up your forum and how to customize it to suit your needs.

Requirements
============

Python 2.7+ or 3.3+, Django 1.8+. Please refer to the requirements_ section of the documentation for a full list of dependencies.

.. _requirements: https://django-machina.readthedocs.org/en/latest/getting_started.html#requirements

Demo sites
==========

Two demo sites can be tested:

* the `vanilla project <http://vanilla.machina-forum.io/>`_ contains a standard installation of *django-machina* without customization
* the `demo project <http://demo.machina-forum.io/>`_ showcases the customization possibilities of *django-machina*

Authors
=======

Morgan Aubert (`@ellmetha <https://github.com/ellmetha>`_) and contributors_

.. _contributors: https://github.com/ellmetha/django-machina/contributors

License
=======

BSD. See ``LICENSE`` for more details.
