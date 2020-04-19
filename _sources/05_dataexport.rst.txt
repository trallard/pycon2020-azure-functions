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

|floppy| Additional resources and docs
---------------------------------------

- `Azure functions triggers and bindings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure functions supported bindings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#supported-bindings?WT.mc_id=pycon_tutorial-github-taallard>`_
- `Azure Storage documentation <http://azure.microsoft.com/documentation/articles/storage-create-storage-account?WT.mc_id=pycon_tutorial-github-taallard>`_ 
