|pipe| Data processing with functions
=========================================

We already have a working and deployed function, but so far it is not doing anything exciting.

Let's start working on the data processing part of the function.

The details
-------------
To demonstrate the capabilities of Azure functions for data processing scnearios we will build the followign pipeline:

#. Collect data from the `StackOverFlow API to create out pipeline <https://api.stackexchange.com/>`_ using the timer trigger.
#. Store the raw data in our Azure storage account.
#. Trigger the processing function that cleans the data and leaves it in a usable format.

Let's get started!

