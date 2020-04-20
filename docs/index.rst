.. Easy data processing on Azure with Serverless Functions documentation master file, created by
   sphinx-quickstart on Wed Apr 15 11:37:06 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|cloud-computing| Easy data processing on Azure
---------------------------------------------------------

with Serverless Functions
---------------------------------------------------------

Welcome to the data processing with Azure functions workshop!
This was initially planned to be delivered at PyCon US 2020 but is now available online as part of the online efforts by the amazing PyCon staff.

.. image:: _static/icons/MSFT_Logo_Color.png
   :class: inline-image
   :width: 80%
   :align: center
   :alt: Microsoft logo


Description
--------------
Serverless computing (also known as function as a service, FaaS) is a design pattern where applications are hosted by a third-party service (i.e. Azure). Eliminating the need for server software and hardware management by the developer.

Serverless can be an excellent alternative for Pythonistas interested in data processing as it allows them to focus on their code rather than the cloud infrastructure. This workshop will introduce attendees to Azure Functions for data processing scenarios (including data acquisition, cleaning and transformation and storage for subsequent usage).

After this tutorial, attendees will have had practical experience with Azure functions for data processing scenarios. Also, they will leave the workshop with a basic function for data processing that could be further modified/extended to suit their needs/requirements.

Outline
*********

1. Introduction to serverless and Azure functions
2. Creating your first Azure function:
   - Create a simple scheduled function using the VS Code extension
   - Familiarise with functions projects and structure
   - Running and debugging locally
3. Functions deployment
   - Deploy your function to Azure
   - Familiarise with the Azure portal
4. Data processing use case
   - Updating your function to collect data
   - Data cleaning, aggregation and storage


Pre-requisites
*********************

This workshop is aimed at folks interested in data processing, data engineering or data science. The goal is to provide a practical introduction to serverless for data processing scenarios.


We assume that you:

- Have intermediate Python knowledge:

   - Have a good understanding of how to write and call functions
   - Have a good knowledge of how Python modules and scripts work

- Have some experience with data wrangling and/or data processing (not extensive experience required but have, for example, used libraries like pandas and requests for data wrangling and API access)

- Are comfortable using the command line/terminal (no need to be an expert but should be comfortable enough to navigate file systems and perform necessary Git tasks)

The setup and other instructions to set your development environment can be found in the :ref:`setup` section of this tutorial.
Make sure to follow these instructions before continuing with the rest of the tutorial.


.. toctree::
   :maxdepth: 2
   :caption: Tutorial Table of Contents:

   self
   setup
   01_introduction
   02_functions_intro
   03_functions_deploy
   04_data_function
   05_data_export
   06_complete_scenario
   glossary