ansible-modules
###############

A repository of Ansible modules.

Installation
------------

To use these modules, add a git submodule under the ``library`` directory at the
root of the playbooks directory::

    mkdir library
    touch library/__init__.py
    git submodule add https:/www.shore.co.il/cgit/ansible-modules library/shore

To update the submodule ::

    git submodule update --remote library/shore

Remember to commit ``.gitmodules``!

Modules
-------

- <placeholder>

License
-------

AGPL v3+

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/cgit/.

TODO
----

- Test installation and update instructions.
