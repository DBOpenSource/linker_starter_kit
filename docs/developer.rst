====================
Notes For Developers
====================



Build pypi package
------------------

.. code-block:: none

    python3 setup.py sdist bdist_wheel upload -r pypi


Build Documentation
-------------------

.. code-block:: none

    cd docs
    make clean
    make html
    cd ..
    python3 setup.py upload_docs --upload-dir docs/_build/html

