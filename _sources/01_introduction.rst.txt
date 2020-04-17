Introduction to serverless and Azure functions
================================================

|light| What are functions?
----------------------------

Functions allow you to run code in a serveless fashion. This means two things:

#. The infrastructure is abstracted from the developer (you) as it is dynamically assigned by Azure.
#. It is completely on demand you only pay for what you consume.

The following infographic provides more details on how serverless functions work:

.. image:: _static/images/serverless.png
    :alt: serveless infographic


Functions are very versatile - you can use a variety of triggers to call your functiond and execute your code. 
They can be set so that they always run the same task or to run specific tasks based on inputs.

Azure provides three main plans for functions, which will determine the kind of instances used, execution times and pricing.

For more details check the `Azure functions consumption plans <https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale?WT.mc_id=pycon_tutorial-github-taallard>`_ docs.

.. note:: Since serverless functions are meant to be stateless, the resources inside the function will disappear once the code had finished executing (or the timeout is reached).


|floppy| Additional resources and docs
---------------------------------------


- `Introduction to Azure functions <https://docs.microsoft.com/azure/azure-functions/functions-overview?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Azure functions consumption plans <https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Functions app timeout <https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout?WT.mc_id=pycon_tutorial-github-taallard>`_ 
- `Azure Storage docs <https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction#core-storage-services?WT.mc_id=pycon_tutorial-github-taallard>`_ 