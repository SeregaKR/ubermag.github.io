=======
ubermag
=======

The meta-package ``ubermag`` does not directly provide any additional
functionality. It is generally not intended for being used directly. Its main
purpose is to ensure that a consistent set of Ubermag subpackages is installed.

The meta-package can also be used to run the tests of all Ubermag subpackages:

.. code-block:: python

   import ubermag
   ubermag.test()

.. toctree::
    :maxdepth: 1
    :caption: ubermag
    :glob:

    notebooks/ubermag/hdf5-file-specification
