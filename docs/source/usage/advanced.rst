Advanced usage
==============

File Structuring
----------------
You can structure and organize your documentations files using file
structures.

And here's how you organize ``.rst`` files into your documentation page:

.. code:: rst
    .. toctree::
        .rst file 1
        /subdirectory/index
        .rst file 2

In your ``index.rst``, add ``.rst`` files under ``.. toctree::``, then they will appear
as a child page of your index page.

You can also organize sections of documentaion into subdirectories and you can
add them to your doc tree as well.

Localization of Documentation
------------------------------

Adding Additional languages to your documentation can be done
by creating another git project, then go to `document project page <https://readthedocs.org/projects/mza79-rtd-tutorial/>`_
, click :guilabel:`⚙ Admin`, and go to translations, add the project and select the language.
Then you can see the languages option in the ``flyout menu``.

For more details in Localization support, you can visit the `Read the Docs Documentation <https://docs.readthedocs.io/en/stable/localization.html>`_
