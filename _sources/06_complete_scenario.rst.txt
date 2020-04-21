|3d| Completing the scenario
==============================

To finish the scenario we are going to do the following:

- Create a new function that will have as trigger the Blob Storage file creation
- Send automated emails with the URLs from the questions

Let's go.

1. Create your new function
------------------------------

Creating a new function in an existing functions project is very similar to the process we followed in section :ref:`functions101`.

Inside the same VS Code workspace we have been using until now:

#. Click on the Azure extension on the sidebar.
#. In the Azure functions section click on the **Create function** icon.

    .. image:: _static/images/snaps/new_function.png
            :align: center
            :alt: Create function

#. Select the **Azure Blob storage trigger** and **AzureWebJobsStorage**.
#. Finally provide the blob path to be monitored: ``functionblob/{name}``.

Your new `function.json` file should look like this:

    .. literalinclude:: ../solutions/03-full-pipeline/blob-manipulation/function.json
        :language: json
        :caption: blob-manipulation/function.json

.. tip:: You can also filter based on file extension, for example ``functionblob/{name}.csv``

2. Create email binding
------------------------------

|floppy| Additional resources and docs
---------------------------------------

- `Azure Blob Storage trigger docs <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Blob name patterns <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#blob-name-patterns>`_
- `Azure Blob storage input binding <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?tabs=python>`_
