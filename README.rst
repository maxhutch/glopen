glopen
======
|Version Status| |Downloads|

Open-like context managers for remote globus files.

``glopen(filename, mode, endpoint)``:
 
1. Creates a temporary file
2. [On a read mode:] Transfers the remote file to the temporary file
3. Opens the temporary file with the given mode
4. Yields the open temporary file
5. Closes the temporary file
6. [On a write mode:] Transfers the temporary file to the remote file
7. Deletes the temporary file

``glopen_many(filenames, mode, endpoint)`` takes a list of filenames and yeilds a list of open files.  
The remote copies are grouped into a single globus transfer, improving performance for small files.

Example
-------
.. code:: python

    >>> from glopen import glopen
    >>> with glopen("path/to/remote/file.anything", mode="r", 
                    endpoint="globusid#endpoint") as f:
    ...     lines = f.readlines()

    >>> from glopen import glopen_many
    >>> files = ["file1", "file2", "file3"]
    >>> with glopen_many(files, mode="w", endpoint="globusid#endpoint") as fs:
    ...     for f,d in zip(fs,d):
    ...         f.write(d)

Install
-------

``glopen`` is on the Python Package Index (PyPI):

::

    pip install glopen

It depends on globussh_, a light-weight wrapper around the globus SSH interface.
Your local machine must be a globus endpoint, so you can either run `Globus connect personal`_ or `Globus connect server`_.

Configuration
-------------

``glopen`` transfers files to and from a temporary directory on your local machine, 
so it needs to know the machine's endpoint name and a directory that globus can access.
You tell ``glopen`` the endpoint and temporary directory in a ``~/.glopen`` config file:

::

    {
      "local_endpoint" : "<globusid>#<endpoint_name>",
      "tempdir" : "/home/<username>/tmp"
    }

.. |Version Status| image:: https://pypip.in/v/glopen/badge.png
   :target: https://pypi.python.org/pypi/glopen/
.. |Downloads| image:: https://pypip.in/d/glopen/badge.png
   :target: https://pypi.python.org/pypi/glopen/
.. _globussh: https://github.com/maxhutch/glopen
.. _Globus connect personal: https://www.globus.org/globus-connect-personal
.. _Globus connect server: https://www.globus.org/globus-connect-server

