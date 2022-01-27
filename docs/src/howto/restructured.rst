Restructured Text
=================

https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html

Format
------

*italic*

**bold**

``code``

#. First
#. Second


Admonitions
-----------

.. caution::
	some warnings

.. danger::
	danger text

.. tip::
	text

.. note::
	text

Images
------

.. image:: ../images/lion.png
    :width: 50px
    :align: center
    :height: 80px

Tables
------
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

.. csv-table:: Title Name
   :header: "A", "B", "A and B"
   :widths: 15, 10, 30

   "False", "False", "False"
   "True", "False", "False"
   "False", "True", "False"
   "True", "True", "True"

Code
----
.. code-block:: python
    :linenos:

    def say_hello(name):
        print("hello " + name)

Hyperlink
---------
https://www.google.ch

`Google <https://www.google.ch>`_

Here you find more information for `reStructuredText`_

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
