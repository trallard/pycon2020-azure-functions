Introduction to serverless and Azure functions
================================================

|light| What is serverless computing?
---------------------------------------

Serverless is also known as Function as a Service (FaaS).

In a nutshell:

#. Serverless architecture makes use of third-party services. They might, for example, run your code on managed, ephemeral containers in a FaaS platform (Azure functions).
#. Servers are still used to run your applications. But in this case, your cloud provider takes care of the management, provisioning and scaling (Microsoft Azure in this case).

This allows you to focus on the code and deploy when ready, while your provider takes care of the infrastructure.

Some of the advantages of serverless are:

- They are scalable: not only this scales automatically based on the increase and decrease in usage but also is highly available.
- It can save you money: you pay only for the usage (number of executions) instead of for having a server running 24/7.

The following infographic provides more details about serverless:

.. image:: _static/images/serverless.png
    :alt: serverless infographic

|faas| Azure functions and serverless
----------------------------------------

FaaS allows you to run self-contained code snippets called **functions** in the cloud. 
Your functions are idle until particular events trigger them. 
Functions are self-contained, small, short-lived, and single-purpose. 
They disappear after execution - hence why they are called ephemeral.

Functions are very versatile - you can use a variety of triggers to call your function and execute your code. 
They can be set so that they always run the same task or to run specific tasks based on inputs.

Microsoft Azure's FaaS is called `Azure Functions <https://azure.microsoft.com/en-gb/services/functions?WT.mc_id=pycon_tutorial-github-taallard>`_.
This FaaS already supports multiple programming languages:

.. image:: https://azurecomcdn.azureedge.net/cvt-e918f8bc2be525756af58617c14443351ac83a8fd87a0b28d31919d627969098/images/page/services/functions/value-prop-5.svg
    :alt: Functions languages

So we are going to take advantage of the Python support for this tutorial.

Azure provides three main plans for functions, which will determine the kind of instances used, execution times and pricing.

For more details, check the `Azure functions consumption plans <https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale?WT.mc_id=pycon_tutorial-github-taallard>`_ docs.

.. note:: Since serverless functions are meant to be stateless, the resources inside the function will disappear once the code had finished executing (or the timeout is reached).


|floppy| Additional resources and docs
---------------------------------------


- `Introduction to Azure functions <https://docs.microsoft.com/azure/azure-functions/functions-overview?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Azure functions consumption plans <https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Functions app timeout <https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Azure Storage docs <https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction#core-storage-services?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Infographic high-res pdf <https://github.com/trallard/tech-bites/tree/master/EN/serverless>`_  CC-BY
