# ⚡️ 🐍 Easy data processing with Azure functions and Python

[![License](https://img.shields.io/badge/License-MIT-gray.svg?colorA=2D2A56&colorB=7A76C2&style=flat.svg)]((https://opensource.org/licenses/MIT))
![docs](https://github.com/trallard/pycon2020-azure-functions/workflows/docs/badge.svg)

This repository contains the tutorial for the Azure Sponsored workshop as well as the solutions.

:sparkles: You can access  the tutorial (self-paced) at <https://aka.ms/pycon2020-azurefunctions>.

The solutions are located in this repository in the [solutions](./solutions) directory.

:sparkles: There is also a video that will be released in the upcoming weeks.

## Table of Contents
- [⚡️ 🐍 Easy data processing with Azure functions and Python](#️--easy-data-processing-with-azure-functions-and-python)
  - [📝 Description](#-description)
  - [🔖 Outline](#-outline)
  - [💻 Pre-requisites](#-pre-requisites)
  - [👀 Solutions](#-solutions)
  - [License](#license)

## 📝 Description

Serverless computing (also known as function as a service, FaaS) is a design patters where applications are hosted by a third-party service (i.e. Azure) eliminating the need for server software and hardware management by the developer.  

Serverless can be an excellent alternative for Pythonistas interested in data processing as it allows them to focus on their code rather than the cloud infrastructure. This workshop will introduce attendees to Azure Functions for data processing scenarios (including data acquisition, cleaning and transformation and storage for subsequent usage). 

After this tutorial, attendees will have had practical experience with Azure functions for data processing scenarios. Also, they will leave the workshop with a basic function for data processing that could be further modified/extended to suit their needs/requirements.

## 🔖 Outline

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
   - Data cleaning, agreggation and storage


## 💻 Pre-requisites

This workshop is aimed at folks interested in data processing, data engineering 
or data science. The goal is to provide a practical introduction to serverless for data processing scenarios.

We assume that you:

- Have intermediate Python knowledge:
  - Have a good understanding on how to write and call functions
  - Have a good understanding on how Python modules and scripts work

- Have some experience with data wrangling and/or data processing (not extensive experience required but have, for example, used libraries like pandas and requests for data wrangling and API access)

- Are comfortable using the command line/terminal (no need to be an expert but should be comfortable enough to navigate file systems and perform necessary Git tasks)

## 👀 Solutions

The solutions can be found in the [solutions directory](./solutions) in thid repository.

- Timer function: [API data acqusition only](./solutions/01-timer-function-data-acquisition/)
- Timer function: [API + Blob binding](./solutions/02-timer-function-Blob-binding/)
  
ARM templates included:
- [Storage account and Blob Storage](./solutions/../storage-blob-container/azuredeploy.json)


## License

The contents in this repo are licensed under the (https://opensource.org/licenses/MIT)(MIT) OSI license.

The icons used in the tutorial were created by [Smashicons](https://www.flaticon.com/authors/smashicons) from [Flaticon](https://www.flaticon.com/).
