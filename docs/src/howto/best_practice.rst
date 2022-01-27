.. _best_practice:

Best practice
=============

Imports
-------

- Don’t use relative imports. Exceptions:
    - Skip namespace in ``__init__.py``

- Order the imports alphabetically
- Do not use an alias of imports unless it’s a common one:
  ``import numpy as np``

Pylint & Tests
--------------

- Place an empty ``__init__.py`` into your test folder, otherwise ``pylint`` does not check the test-files.


Type hints
----------

- Use whenever possible and meaningful the syntax provided by
  `PEP 484 – Type Hints <https://www.python.org/dev/peps/pep-0484/>`__.

Unit Tests
----------

- A unit test has a descriptive name:
  ``test___unit_of_work___scenario___expected_behaviour``

    - ``unit_of_work``: What do I test?
    - ``scenario``: How do I test?
    - ``expected_behaviour``: What do I expect?

- A unit test has in most cases three parts which are separated with a
  blank line:

    1. | **Arrange:**
       | Initialize all variables you need for the test, this includes
         also your expected values for the asserts at the end.
         Additionally, set up all necessary context which is needed for
         the test.

    2. | **Act:**
       | Run code under test. Keep this section small, run really only
         the function which you want to test. If the function relies on
         other functions to be called first, make sure they are already
         tested and call them for example in the fixture or as a part of
         *Arrange*.

    3. | **Assert:**
       | Check your expectations with asserts. Use whenever possible a
         specialized ``assert`` of your test-framework instead a generic
         one. For example:

        .. code:: python

            with pytest.raises(RuntimeError):
                parse_metadata('{}', mode=IoModes.STRICT)
