What is pymake2?
################

.. image:: assets/images/pymake2-banner.png
.. image:: https://img.shields.io/travis/philiparvidsson/Pymake2-Build-Tool.svg
   :target: https://travis-ci.org/philiparvidsson/Pymake2-Build-Tool

.. image:: https://img.shields.io/github/license/philiparvidsson/Pymake2-Build-Tool.svg
   :target: https://en.wikipedia.org/wiki/MIT_License


**Pymake2** is a tool for automating build tasks. It comes with ready-made templates for several different kinds of projects, allowing you to quickly set up portable build tasks. **With pymake2, it becomes trivial to set up complex build tasks, doing everything from library and executable compilation to asset building and even deployment.**

* `Download <https://github.com/philiparvidsson/pymake2/releases/>`_
* `Manual <docs/manual.rst>`_

Getting Started
===============
1. Download and install `Python 2.7 <https://www.python.org/downloads/>`_.
2. Start with one of the `examples <examples>`_ or `template <src/pymake2/template>`_ scripts, picking one relevant to your type of project.
3. Modify the script as needed for your project. See the `manual <docs/manual.rst>`_ for instructions on how to do so.
4. Build your project by running your make script. You can either type :code:`python your_make_file.py` or :code:`./your_make_file.py` (only on Linux).

Prerequisites
-------------
* `Python 2.7 <https://www.python.org/downloads/>`_

Installation
------------
**Begin by downloading and installing Python 2.7.**

On Linux, depending on your distribution, Python comes pre-installed. This means that you do not need to install anything for pymake2 to work. If you don't have Python (you can check by typing python in a terminal), you might be able to install it by typing :code:`sudo apt-get install python`.

On Windows, you need to install Python manually. See `this link <https://wiki.python.org/moin/BeginnersGuide/Download>`_ for more information.

**Download the latest pymake2 release.**

The latest pymake2 scripts are always available `here <https://github.com/philiparvidsson/pymake2/releases/>`_. Download and save pymake2.py along with any make script you need for your project.

Usage
-----
To familiarize yourself with pymake2, you can begin by writing a simple make script. You could also use one of the `example scripts <examples>`_, or the one below if you just want to try out pymake2 quickly. In case you use the script below, make sure to put pymake2 in the same directory.

.. code-block:: python

   #!/usr/bin/env python
   from pymake2 import *

   @target
   @depends_on('build', 'compile')
   def all(conf):
       print 'done.'

   @target
   def build(conf):
       print 'building', conf.name + '...'

   @target
   def compile(conf):
       print 'compiling...'

   pymake2({ 'name': 'some_program.bin' })

Since pymake2 scripts are written in Python, there is really no limit to what can be done. This allows you to easily create very complex and secure build and deployment scripts for your projects.

**Build your project.**

Save your script in a file named :code:`make.py` in your project directory. Make sure you have installed pymake2 into the build directory (this is the standard directory, but can always be changed if needed). Invoke your make script by running it with the following command: :code:`python make.py`

Running the Tests
=================
Run the tests by typing :code:`python runtests.py` in the src/tests directory. All tests in the tests directory will be built and run automatically, ending with a report of passing and failing tests, as well as how much time it took to run them.

Deployment
==========
Deploying pymake2 make scripts is easy! You only need to store a copy of pymake2 and your make script in the project directory.

Deploying make scripts
----------------------
Along with your make.py file containing your make logic, you need to store the pymake2 file in your project. Normally, pymake2 should be stored in a directory named build in your project's root.

Built With
==========
* **Emacs** - Emacs is, along with vi, one of the two main contenders in the traditional editor wars of Unix culture. Both are among the oldest application programs still in use.
* **Python** - A widely used high-level, general-purpose, interpreted, dynamic programming language.

Contributing
============
Please read CONTRIBUTING.rst for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
==========
We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/philiparvidsson/pymake2/tags>`_.

Authors
=======
* **Philip Arvidsson** - *Initial work* - `philiparvidsson <https://github.com/philiparvidsson>`_

See also the list of `contributors <https://github.com/philiparvidsson/pymake2/contributors>`_ who participated in this project.

License
=======
This project is licensed under the MIT License—see the `LICENSE <LICENSE>`_ file for details.

Acknowledgments
===============
n/a
