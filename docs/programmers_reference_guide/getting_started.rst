GETTING STARTED
===============

How to Install and Run Jupylet
------------------------------

If you are new to Python, I strongly recommend that you install and use the
`Miniconda Python <https://docs.conda.io/en/latest/miniconda.html>`_
distribution. Download and run the 64-bit installer and stick to the default
install options.

Once Miniconda is installed start a Miniconda Prompt. To do this on Windows
click the :guilabel:`⊞ Winkey` then type *Miniconda* and press the
:guilabel:`Enter` key. This should open a small dark window that programmers
call *console* or *shell* in which you can enter commands and run programs.

To run *jupylet* first install it by typing the following command in the
console:

.. code-block:: bash

    pip install jupylet

Next, you need to download the *jupylet* repository since it contains the
example notebooks. If you have `Git <https://git-scm.com/>`_ installed you
can use it to clone the *jupylet* repository with:

.. code-block:: bash

    git clone https://github.com/nir/jupylet.git

Alternatively, if you don't have Git installed, you can download and unzip
the *jupylet* archive by typing:

.. code-block:: bash

    python -m wget https://github.com/nir/jupylet/archive/master.zip
    python -m zipfile -e jupylet-master.zip .
    move jupylet-master jupylet

.. note::
    On Mac OS X or Linux type *mv* instead of *move* in the command above.

Next, enter the *jupylet/examples/* directory with the change directory
command:

.. code-block:: bash

    cd ./jupylet/examples/

And start a jupyter notebook with:

.. code-block:: bash

    jupyter notebook spaceship.ipynb

Run the notebook by following the instructions in the notebook and a game
canvas should appear with the spaceship example:

.. image:: ../images/spaceship.gif

Python Programming Language
---------------------------

Python is an awesome programming language. It is both simple for kids to
learn and powerful enough to be `one of the most popular programming languages
<https://www.tiobe.com/tiobe-index/>`_ among computer scientists and
programmers.

However, this reference guide is not designed to teach the Python programming
language. If you don't already have a working knowlege of Python and how to
use it to program, I would like to suggest a few resources that may help you
get started:

- `Microsoft's introduction to Python <https://docs.microsoft.com/en-us/learn/modules/intro-to-python/1-introduction>`_
  \- Microsoft has a long tradition of publishing good guides to programming
  languages and this tutorial appears to be in line with this tradition.

- `Python's own tutorial <https://docs.python.org/3/tutorial/index.html>`_
  \- Perhaps not as didactic as Microsoft's guide, but it is a good idea to
  get familiar with Python's documentation.

These guides will instruct you how to start a python interpreter where you
can type and run Python code. You may do that, but once you gain a little bit
of confidence or if you feel adventurous try starting a Jupyter notebook
instead of a simple python interpreter.

To do that start the Miniconda Prompt
`as explained above <#how-to-install-and-run-jupylet>`_, then change
directory into the *jupylet/examples/* directory and start a new notebook by
typing:

.. code-block:: bash

    jupyter notebook hello-world.ipynb

Jupyter Notebooks
-----------------

Jupyter notebooks are a powerful tool but they can be a little confusing at
first. Here are a few resources that explain how to use them:

- *jupylet/examples/hello-world.ipynb* notebook contains some instructions on
  how to use Jupyter notebooks. Check it out.

- `Running Code <https://mybinder.org/v2/gh/jupyter/notebook/master?filepath=docs%2Fsource%2Fexamples%2FNotebook%2FRunning%20Code.ipynb>`_
  \- This is a Jupyter notebook explaining how to use Jupyter notebooks 🙂.
  It is in fact a live notebook running in a web service called mybinder. The
  first time you click it may take a moment to start, so give it that moment.
  Since it is "live" you can play around with it. It works!

- `Jupyter's documentation <https://jupyter-notebook.readthedocs.io/en/latest/notebook.html>`_
  \- There's a whole lot of text in there.

