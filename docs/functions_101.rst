Creating your first Azure function
=====================================

We will start by creating your first Azure function. 
We will make use of VS Code to create a function that works every day at the same time. 


Creating your local project
----------------------------

#. Create a new folder in your local computer. For example if using the command line:

.. code-block:: bash 

    mkdir python-functions

    cd python-functions 

#. Open VS Code and the project folder you just created.

#. Click on the Azure icon on your activity bar
#. Then, in the Azure functions area select the Create new project icon

.. image:: _static/images/snaps/vs_code_functions1.png
    :height: 600px
    :align: center

#. Provide the following information:
    - **Select a language**: Python
    - **Select a Python alias to create a virtual environment**: Select your preferred Python interpreter (needs to be supported)
    - **Select a template**: Timer function
    - **Authorization level**: choose Anonymous

.. code-block:: 

    .
    └── timer-function
        ├── __init__.py
        ├── function.json
        └── 