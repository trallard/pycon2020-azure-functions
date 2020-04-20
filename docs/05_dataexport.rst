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

1. Add Azure Blob Storage
******************************************

We already created a Storage Account in the :ref:`deployfn` section. The next step will be creating a Blob Storage container so we can start saving the data collected through your function.

For simplicity I have provided an ARM (Azure Resource Management) template in |repo| to make it easier for you to create your container.

1. Click on the Deploy to Azure button below:

.. raw:: html

    <a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Ftrallard%2Fpycon2020-azure-functions%2Fmaster%2Fstorage-blob-container%2Fazuredeploy.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true" style="border:none; box-shadow:none; align:center;"/>
    </a>

2. This will redirect you to |azureportal|. Once there complete the following information:

    - **Subscription**: use the same you have been using for the tutorial.
    - **Resource group**: Choose the resource group where your function was created.
    - **Storage Account name**: the name of the storage account you created when deploying your account.
    - **Container name**: provide a name for your container.

3. Tick the **I agree to the terms and conditions** box and click the  **Purchase** button.

    .. image:: _static/images/snaps/blobarm.png
        :align: center
        :alt: Storager create

    This will trigger the deployment of the Blob and you should be able to see the deployment status displayed on the top left.
4. Still on |azureportal| click on **Storage accounts** on the sidebar and then on the corresponding storage account.

    .. image:: _static/images/snaps/storagedashboard.png
        :align: center
        :alt: Storager dashboard

5. In the next window click on **Access keys** and copy the Connection string.

    .. image:: _static/images/snaps/access.png
            :align: center
            :alt: Storager dashboard access

6. Back in VS Code click on the **Azure** extension on the sidebar and then right-click on your function name > **Add binding**.
5. Since we want to store the outputs in the container, we need to select the **OUT** direction followed by **Azure Blob Storage**.
7. Assign a name for the binding a path for the blob:

    .. code-block::

        functionblob/{DateTime}.csv

    Notice that I am using the name of the container I created before and the binding expression ``DateTime`` which  resolves to ``DateTime.UtcNow``. The following blob path in a ``function.json`` file creates a blob with a name like ``2020-04-16T17-59-55Z.txt``.

8. Select **AzureWebJobsStorage** for your local settings. 

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

|floppy| Additional resources and docs
---------------------------------------

- `ARM template for Blob Storage container <https://github.com/trallard/pycon2020-azure-functions/tree/master/storage-blob-container>`_
- `Azure functions triggers and bindings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure functions supported bindings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#supported-bindings?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure Storage documentation <http://azure.microsoft.com/documentation/articles/storage-create-storage-account?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Binding expressions docs <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure function reference output <https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#outputs?WT.mc_id=pycon_tutorial-github-taallard>`_

