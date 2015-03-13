glopen
======
|Version Status| |Downloads|

Open-like context managers for remote globus files.

Example
-------
.. code:: python

    >>> from glopen import glopen
    >>> with glopen("path/to/remote/file.anything", mode="r", endpoint="globusid#endpoint") as f:
    ...    lines = f.readlines()

    >>> from glopen import glopen_many
    >>> files = ["file1", "file2", "file3"]
    >>> with glopen_many(files, mode="w", endpoint="globusid#endpoint") as fs:
    ...     for f,d in zip(fs,d) :
    ...         f.write(d)

Install
-------

``glopen`` is on the Python Package Index (PyPI):

::

    pip install glopen


.. |Version Status| image:: https://pypip.in/v/slict/badge.png
   :target: https://pypi.python.org/pypi/slict/
.. |Downloads| image:: https://pypip.in/d/slict/badge.png
   :target: https://pypi.python.org/pypi/slict/

