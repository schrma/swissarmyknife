.. _set_up:

======
Set Up
======

Install instructions
====================

Windows
-------

Install dependencies
~~~~~~~~~~~~~~~~~~~~

Go to python-package-pixiepy root directory. Create and activate python
virtual environment:

.. code:: bash

   python -m venv .venv-swiss
   .venv-swiss/Scripts/activate.bat


Install package and its dependencies:

.. code:: bash

   pip install -e .[testing]

Running tests
=============

**Make sure your environment is activated.**

.. code:: bash

   pytest

Sphinx
======

.. code-block:: shell

    sphinx-build --color -b html -d "./docs/_build/doctrees" "./docs" "./docs/_build/html"

or

.. code-block:: shell

    tox -e docs

Publish to Pypi
===============

.. code-block:: shell

    git tag 0.0.4

.. code-block:: shell

    python -m twine check dist/*
    python -m twine upload dist/*

or

.. code-block:: shell

    tox -e publish

Pylint
======

.. code-block:: shell

    pylint --rcfile=setup.cfg src/swissarmyknife tests

or

.. code-block:: shell

    tox -e pylint

Flake8
======

.. code-block:: shell

    flake8 src/swissarmyknife tests

or

.. code-block:: shell

    tox -e flake8