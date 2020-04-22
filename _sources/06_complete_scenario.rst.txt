|3d| Completing the scenario
==============================

To finish the scenario, we are going to do the following:

- Create a new function that will have as trigger the Blob Storage file creation
- Send automated emails with the URLs from the questions

Let's go.

1. Create your new function
------------------------------

Creating a new function in an existing functions project is very similar to the process we followed in section :ref:`functions101`.

Inside the same VS Code workspace we have been using until now:

#. Click on the Azure extension on the sidebar.
#. In the Azure functions, section click on the **Create function** icon.

    .. image:: _static/images/snaps/new_function.png
            :align: center
            :alt: Create function

#. Select the **Azure Blob storage trigger** and **AzureWebJobsStorage**.
#. Finally provide the blob path to be monitored: ``functionblob/{name}.csv``.

As before, I am going to rename the ``scriptFile`` to ``blob_manipulation.py`` to keep my workspace tidy.

Your new `function.json` file should look like this:

    .. literalinclude:: ../solutions/03-full-pipeline/blob-manipulation/function.json
        :language: json
        :caption: blob-manipulation/function.json

.. note:: Here we are filtering by file extension and path ``functionblob/{name}.csv``. For more patterns, check the `Blob name patterns docs <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#blob-name-patterns>`_.

2. Add bindings
------------------------------
We need to create two more output bindings:

- SendGrid: we will use this to send the daily email
- Azure Blob Storage: we will save the output figures Here

Blob Storage
******************************

#. Attach a Blob storage binding. We are going to follow the same process as in section :ref:`attachblob`. Follow this similar configuration:

    .. code-block:: json

        {
        "type": "blob",
        "direction": "out",
        "name": "outputBlob",
        "path": "functionblob/{name}_tag_plot.png",
        "connection": "AzureWebJobsStorage"
        }

SendGrid by Twilio
******************************

#. Head to |azureportal|. On the left sidebar click on **+ Create a resource**. Then on the Search Bar Type **SendGrid**.
#. Click on the **Create** button.

    .. image:: _static/images/snaps/sendgrid.png
        :align: center
        :alt: Create sendgrid

#. Fill the details in the create form - make sure to select the same resource group we have been using. As an Azure customer, you get 25000 emails free per month. Once completed, click on **Review + Create ** and **Create**.

#. You will a progress bar on top of your screen, click on it and wait for your deployment to complete. Once completed, click on **Go to resource**.


    .. image:: _static/images/snaps/sendgrid2.png
            :align: center
            :alt: Create sendgrid

#. Click on the **Manage** tab.

    .. image:: _static/images/snaps/sendgrid3.png
        :align: center
        :alt: Sengrid manage

#. You will be redirected to your`SendGrid dashboard <https://app.sendgrid.com>`_. Once there click on **Settings**  > **API Keys** > **Create API Key**.

    .. image:: _static/images/snaps/sendgrid4.png
        :align: center
        :alt: Create API key

#. In the next screen give your key a name, select **Full Access** and then **Create & view**.

    .. image:: _static/images/snaps/sendgrid5.png
        :align: center
        :alt: Create API key

Make sure to take note of your API key as we will need it to add the binding.




|floppy| Additional resources and docs
---------------------------------------

- `Azure Blob Storage trigger docs <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Blob name patterns <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#blob-name-patterns?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure Blob storage input binding <https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?tabs=python?WT.mc_id=pycon_tutorial-github-taallard>`_
- `SendGrid by Twilio <https://sendgrid.com/docs/>`_
- `SenGrid Python API <https://github.com/sendgrid/sendgrid-python>`_
- `SendGrid API - POST email <https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md#post-mailsend>`_
