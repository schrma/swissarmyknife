.. _how_to_write_an_app:

How to write an App
===================

Writing a console application in python is quite easy. Basically, every
script is a kind of application. The tricky part is to test it,
therefore we suggest the following structure to achieve almost 100%
coverage.

Application
-----------

You should implement the following functions in your application-script.
The script should be placed in *src/pixie/apps*.

1. Necessary imports:

    .. code:: python

       import argparse
       import sys

2. Define ``ArgumentParser``:

    .. code:: python

       def get_parser():
           parser = argparse.ArgumentParser()
           parser.add_argument(...)
           return parser

3. Parse commandline argument to ``dict``:

    .. code:: python

       def parse_command_line_args(args=None):
           parsed_args = get_parser().parse_args(args)
           return vars(parsed_args)

4. Implement ``main``-function:

    .. code:: python

       def main(**kwargs):
           # Implement your app
           return exitcode

5. Add entrypoint to script:

    .. code:: python

       if __name__ == "__main__":
           sys.exit(main(**parse_command_line_args()))

Test
----

.. code:: python

   import shlex
   import pixie.apps.application


   def test___application___golden_run___no_error_raised():
       command_line = \
           " ".join(positional_arguments) + \
           f" -a {argument_a}" \
           f" -b {argument_b}"

       command_line_args = pixie.apps.application.parse_command_line_args(shlex.split(
           command_line,
           posix=os.name == "posix"
       ))
       exitcode = pixie.apps.application.main(**command_line_args)

       assert exitcode == 0
