ansible-modules
###############

.. image:: https://git.shore.co.il/ansible/ansible-modules/badges/master/pipeline.svg
    :target: https://git.shore.co.il/ansible/ansible-modules/-/commits/master
    :alt: pipeline status

A repository of Ansible modules.

This project is deprecated. All of the modules in this repo have equivalents in
the Ansible project making them obsolete. Right now the only tests that are done
are linters with pre-commit.

Installation
------------

To use these modules, add a git submodule under the :code:`library` directory
at the root of the playbooks directory

.. code:: shell

    mkdir library
    touch library/__init__.py
    git submodule add https://www.shore.co.il/git/ansible-modules library/shore master
    sudo pip install -r library/shore/requirements.txt

To update the submodule

.. code:: shell

    git submodule update --remote library/shore

Remember to commit :code:`.gitmodules`!

Modules
-------

- collectd_facts (use the :code:`package_facts` module instead)
- ldap_attr (has been accepted in to the Ansible project)
- nginx_facts (use the :code:`package_facts` module instead)
- dhparams (use the :code:`openssl_dhparams` module instead)

Usage
-----

See example usage in the test playbooks under :code:`tests/`.

License
-------

This software is licensed under the AGPL v3+ license (see the
:code:`LICENSE.txt` file).

Testing
-------

Modules are tested on Ubuntu Precise, Trusty and Xenial and Debian Wheezy,
Jessie and Stretch with Ansible version 2.0.2.0, 2.1.6.0, 2.2.3.0 and 2.3.1.0.
The tests require `Tox <https://tox.readthedocs.io/>`_ and `Docker
<https://docker.com>`_. `Pre-commit <http://pre-commit.com/>`_ is also setup for
this project.

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/explore/.

TODO
----

- Test installation and update instructions.
