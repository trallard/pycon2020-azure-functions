|cloud-computing| Deploy your first function
==============================================

The next step will be to deploy your function to Azure. We will use the VS Code extension again.

1. Click on the Azure extension on the VS Code sidebar (1 in image) and then click on the deploy to function app on the Azure functions section (2 in image).

    .. image:: _static/images/snaps/deploy1.png
        :align: center
        :alt: Prepare for deploy

2. Select the **Create new app option** and then provide a name for your app.
3. Select the correct Python runtime version.
4. Select a location for your resources (this the datacentre where all your resources will be located e.g. Western Europe).
5. Wait for the deployment to complete. You can see the progress on the pop-up window or on your output console.

.. _portalinst:

Using the Azure portal
--------------------------

There are multiple ways to check the status of your function. We will do this from the Azure portal.

#. Head to |azureportal|.
#. Click on the home icon on the sidebar (if the sidebar is hidden you need to click on the ``>>`` icon on the top left corner).
#. The default view should show your new resources. For me, it shows the resource group called ``pycon2020`` as this is the name I gave it.

    .. image:: _static/images/snaps/portal_01.png
            :align: center
            :alt: Azure portal home

#. Click on the resource group that contains your function. You should see the following screen displaying all your resources.

    .. image:: _static/images/snaps/portal_02.png
            :align: center
            :alt: Resource group

#. Click on your function name (see image above) and then on the **monitor** section of the sidebar.

    .. image:: _static/images/snaps/portal_03.png
            :align: center
            :alt: Monitor function

#. In the following screen, you should be able to see the status of your function, the runs and their statuses as well as the URL for your app. You can also click on each individual run to check the logs output.

    .. image:: _static/images/snaps/portal_02.png
            :align: center
            :alt: Resource group

🎉 Congratulations you have deployed your first serverless function! 🥳


|floppy| Additional resources and docs
---------------------------------------

- `Monitoring Azure functions <https://docs.microsoft.com/azure/azure-functions/functions-monitoring?tabs=cmd&WT.mc_id=pycon_tutorial-github-taallard>`_ 
