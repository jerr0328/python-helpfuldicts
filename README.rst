============
helpfuldicts
============


FrozenDict
----------
``FrozenDict`` is an immutable wrapper around dictionaries that implements the
complete mapping interface. It can be used as a drop-in replacement for
dictionaries where immutability is desired.

Of course, this is ``python``, and you can still poke around the object's
internals if you want.

The ``FrozenDict`` constructor mimics ``dict``, and all of the expected
interfaces (``iter``, ``len``, ``repr``, ``hash``, ``getitem``) are provided.
Note that a ``FrozenDict`` does not guarantee the immutability of its values, so
the utility of ``hash`` method is restricted by usage.

The only difference is that the ``copy()`` method of ``FrozenDict`` takes
variable keyword arguments, which will be present as key/value pairs in the new,
immutable copy.

Example shell usage:

.. code-block:: python

    from helpfuldicts import FrozenDict

    fd = FrozenDict({ 'hello': 'World' })

    print fd
    # <FrozenDict {'hello': 'World'}>

    print fd['hello']
    # 'World'

    print fd.copy(another='key/value')
    # <FrozenDict {'hello': 'World', 'another': 'key/value'}>


NonelessDict
------------
``NonelessDict`` is a wrapper around dictionaries that will check if a value is None/empty/False,
and not add the key in that case.
