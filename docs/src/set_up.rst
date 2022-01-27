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
    tox -e docs

