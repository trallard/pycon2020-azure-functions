|pipe| Completing the data scenario
====================================

You should now have working function that collects data from the StackExchange API.

In this section we will:

- Complete the function to store the data in AzureBlob storage
- Create a second function that identifies the addition of a file to Azure Blob storage and triggers a second function
- Create a dabatase to store our cleaned data and modify the function to store the dabatase

|light| Triggers and bindings
--------------------------------

- **Triggers**: these cause a function to run. They can be a HTTP request, a queue message or an event grid. Each function **must** have one trigger.

- **Binding**: is a connection between a function and another resource or function. They can be *input bindings, output bindings* or both. These are optional and a function can have one or more bindings.

1. Create Azure Blob Storage
******************************************

We already created a Storage Account in the :ref:`deployfn` section. The next step will be creating a Blob Storage container so we can start saving the data collected through your function.

#. Head over to |azureportal| and click on **Storage accounts** on the left sidebar and then on your function storage account.

    .. image:: _static/images/snaps/storagedashboard.png
        :align: center
        :alt: Storager dashboard

#. Click on either of the **Containers** section (see image).

    .. image:: _static/images/snaps/containers.png
        :align: center
        :alt: Containers screenshot

#. Click on **+ Container** at the top of the bar and provide a name for your Blob container.

#. Without leaving your dashboard, click on **Access keys** on the sidebar menu and copy the Connection string.

    .. image:: _static/images/snaps/access.png
            :align: center
            :alt: Storage dashboard access

2. Attach Blob binding
******************************************

Now that you created the Blob container you need to add the binding to your function. 

1. Back in VS Code click on the **Azure** extension on the sidebar and then right-click on your function name > **Add binding**.
2. Since we want to store the outputs in the container, we need to select the **OUT** direction followed by **Azure Blob Storage**.
3. Assign a name for the binding a path for the blob:

    .. code-block::

        functionblob/{DateTime}.csv

    Notice that I am using the name of the container I created before and the binding expression ``DateTime`` which  resolves to ``DateTime.UtcNow``. The following blob path in a ``function.json`` file creates a blob with a name like ``2020-04-16T17-59-55Z.txt``.

4. Select **AzureWebJobsStorage** for your local settings. 

Once completed, your ``function.json`` file should look like this:

    .. code-block:: json
        :caption: function.json
        :emphasize-lines: 10-16


        {
            "scriptFile": "main_function.py",
            "bindings": [
                {
                "name": "mytimer",
                "type": "timerTrigger",
                "direction": "in",
                "schedule": "0 0 9 * * *"
                },
                {
                "type": "blob",
                "direction": "out",
                "name": "outputBlob",
                "path": "functionblob/{DateTime}.csv",
                "connection": "AzureWebJobsStorage"
                }
            ]
            }

5. Add the **Storage access key** that you copied before to your ``local.settings.json``

    .. code-block:: json
        :caption: local.settings.json
        :emphasize-lines: 4

        {
            "IsEncrypted": false,
            "Values": {
                "AzureWebJobsStorage": <Your key>,
                "FUNCTIONS_WORKER_RUNTIME": "python",
                "AzureWebJobs.timer-function.Disabled": "false"
            }
        }

3. Update your function
*****************************



|floppy| Additional resources and docs
---------------------------------------

- `ARM template for Blob Storage container <https://github.com/trallard/pycon2020-azure-functions/tree/master/storage-blob-container>`_
- `Azure functions triggers and bindings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure functions supported bindings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#supported-bindings?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure Storage documentation <http://azure.microsoft.com/documentation/articles/storage-create-storage-account?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Binding expressions docs <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure function reference output <https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#outputs?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Python type hints cheatsheet <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>`_
