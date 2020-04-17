.. _setup:

|laptop| Setup and installation
=================================

Welcome to the Azure sponsored workshop for PyCon 2020 (now online)!

This section will guide you through the prerequisites for the workshop.

Each requirement is outlined here with detailed instructions on their installation.

Python 3.x
------------
Make sure to have one of these Python versions installed:

- 3.6
- 3.7
- 3.8

These are the supported versions by Azure Functions. If you already have one installed jump straight to the rest of the setup instructions.

Otherwise, you can follow this fantastic tutorial from  `Real Python <https://realpython.com/installing-python/>`_ to get a clean Python install.

VS Code
--------

We will be using Visual Studio Code (or VS Code for short).
VS Code is an Open Source IDE that can be easily extended or enhanced with extensions.
For this particular tutorial, we will use the Python and the Azure functions extensions.
To get started:

1. Download and install `VS Code <https://code.visualstudio.com//?WT.mc_id=?WT.mc_id=pycon_tutorial-github-taallard>`_ . When directed to the install page, this should identify your OS. Download the install file and follow the instructions.
2. Install the `Python VS Code extension <https://marketplace.visualstudio.com/itemdetails?itemName=ms-python.python&wt.mc_id=?WT.mc_id=pycon_tutorial-github-taallard>`_ . Click on the Install button on the extension website. This will launch VS Code and ask for your confirmation to install.
3. Install the `Azure Functions extension <https://marketplace.visualstudio.com/itemdetails?itemName=ms-azuretools.vscode-azurefunctions&wt.mc_id=?WT.mc_id=pycon_tutorial-github-taallard>`_

Azure account and credits
---------------------------

You can sign up to your Azure account and receive 12 months of some free services as well as 200 USD in credits.
To get started with Azure visit  `this link <https://cda.ms/1fM>`_.

Azure CLI and functions core tool
----------------------------------
- We first need to install the Azure CLI  to be able to deploy our functions

.. tabs::

  .. group-tab:: Mac OSX

    #. Install homebrew
    #. Install the CLI

    .. code-block::

      brew update && brew install azure-cli

  .. group-tab:: Windows

      #. Download the installer from `the docs page <https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest?WT.mc_id=pycon_tutorial-github-taallard>`_ 
      #. When downloaded, open the driver to follow the instructions.

  .. group-tab:: Linux

    The instructions vary depending on your distribution. Please follow the
    instructions in the `official docs <https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest?WT.mc_id=pycon_tutorial-github-taallard>`_ 

- To be able to run and test your functions locally, we need to install the Azure functions core tools:

.. tabs::

  .. group-tab:: Mac OSX

    #. Install homebrew
    #. Install the CLI

    .. code-block::

      brew tap azure/functions
      brew install azure-functions-core-tools@3
      # if upgrading on a machine that has 2.x installed
      brew link --overwrite azure-functions-core-tools@3

  .. group-tab:: Windows

      #. Install `Node.js <https://docs.npmjs.com/getting-started/installing-node#osx-or-windows>`_ 
      #. Install the core tools package

      .. code-block::

        npm install -g azure-functions-core-tools@3

  .. group-tab:: Linux

    For Debian/Ubuntu distributions:

    1. Install  Microsoft package repository GPG key, to validate package integrity:

      .. code-block::

        curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
        sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg

    2. Set up the .NET development source list before doing an APT update.

      .. code-block::

        # Ubuntu
        sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'

        # Debian

        sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs | cut -d'.' -f 1)/prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'

    3. Start the APT source update and install the tools

      .. code-block::

        sudo apt-get update
        sudo apt-get install azure-functions-core-tools

    For more detailed instructions, visit the `corresponding docs <https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Ccsharp%2Cbash?WT.mc_id=pycon_tutorial-github-taallard>`_.


Additional packages
---------------------

You will need to install some packages to follow along with this tutorial. 
To install them follow these steps:

1. Clone the tutorial repository `Repo <https://github.com/trallard>`_ 

  From the command line (bash):

  .. code-block:: bash

      git clone https://github/trallard

      # Change to the directory
      cd azure-functions-pycon

2. Install the main dependencies:

  .. code-block:: bash
