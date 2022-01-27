==============
swissarmyknife
==============

This is a collection of functions which i used frequently including:

* file-handling (reading, writing)
*

.. note::
   This project has been set up using PyScaffold 4.1.2 For details and usage information on PyScaffold see https://pyscaffold.org/.

-------
Content
-------
`Documention <https://swissarmyknife.readthedocs.io/en/latest/>`_

-------------------
Build Documentation
-------------------
Execute the following commands to build the full documentation.



1. Set up virtual environment (must be done only the first time):

.. code-block:: shell

   python -m venv .venv-swiss
   . .venv-swiss/Scripts/activate
   python -m pip install --upgrade pip
   python -m pip install tox

2. Activate your virtual environment:

.. code-block:: shell

   . .venv-swiss/Scripts/activate

3. Execute `tox`

.. code-block:: shell

   tox -e docs
