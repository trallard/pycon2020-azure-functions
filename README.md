# :snake: Easy data processing with Azure functions and Python

[![License](https://img.shields.io/badge/License-MIT-gray.svg?colorA=2D2A56&colorB=7A76C2&style=flat.svg)]((https://opensource.org/licenses/MIT))
![docs](https://github.com/trallard/pycon2020-azure-functions/workflows/docs/badge.svg)

This repository contains the tutorial for the Microsoft Azure Sponsored workshop. As well as all the solutions to the different sections.

<div align="center">
<img src="./docs/_static/icons/MSFT_Logo_Color.png" width="400px">
</div>

:sparkles: You can access the tutorial (self-paced) at <https://aka.ms/pycon2020-azurefunctions>.

:sparkles: The solutions are located in this repository in the [solutions](./solutions) directory.

---

![NEW](https://img.shields.io/badge/-NEW-gray.svg?colorB=18a4e0)  :video_camera:  Tutorial video! Go to the PyCon US Youtube Channel: <https://www.youtube.com/watch?v=PV7iy6FPjAY>

![NEW](https://img.shields.io/badge/-NEW-gray.svg?colorB=18a4e0)  :sparkles: Accompanying slides are on SpeakerDeck <https://speakerdeck.com/trallard/easy-data-processing-on-azure-with-serverless-functions>

---

## Table of Contents

- [:snake: Easy data processing with Azure functions and Python](#snake-easy-data-processing-with-azure-functions-and-python)
  - [Table of Contents](#table-of-contents)
  - [:pencil: Description](#pencil-description)
  - [:bookmark: Outline](#bookmark-outline)
  - [:computer: Pre-requisites](#computer-pre-requisites)
  - [:eyes: Solutions](#eyes-solutions)
  - [License](#license)

## :pencil: Description

Serverless computing (also known as function as a service, FaaS) is a design patterns where applications are hosted by a third-party service (i.e. Azure) eliminating the need for server software and hardware management by the developer.

Serverless can be an excellent alternative for Pythonistas interested in data processing as it allows them to focus on their code rather than the cloud infrastructure. This workshop we introduce attendees to Azure Functions for data processing scenarios (including data acquisition, cleaning and transformation and storage for subsequent usage).

After this tutorial, attendees will have practical experience with Azure functions for data processing scenarios. Also, they will leave the workshop with a basic function for data processing that could be further modified/extended to suit their needs/requirements.

## :bookmark: Outline

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
   - Data cleaning, aggregation and storage

## :computer: Pre-requisites

This workshop is aimed at folks interested in data processing, data engineering or data science. The goal is to provide a practical introduction to serverless for data processing scenarios.

We assume that you:

- Have intermediate Python knowledge:
  - Have a good understanding of how to write and call functions
  - Have a good understanding of how Python modules and scripts work

- Have some experience with data wrangling and/or data processing (not extensive experience required but have, for example, used libraries like pandas and requests for data wrangling and API access)

- Are comfortable using the command line/terminal (no need to be an expert but should be comfortable enough to navigate file systems and perform necessary Git tasks)

## :eyes: Solutions

The solutions can be found in the [solutions directory](./solutions) in this repository.

- Timer function: [API data acqusition only](./solutions/01-timer-function-data-acquisition/)
- Timer function: [API + Blob binding](./solutions/02-timer-function-Blob-binding/)
- Timer function + Data processing/email sending: [full pipeline](./solutions/03-full-pipeline/)

ARM templates included:

- [Storage account and Blob Storage](./solutions/../storage-blob-container/azuredeploy.json)

## :key: License

The contents in this repo are licensed under the [https://opensource.org/licenses/MIT](MIT) OSI license.

The icons used in the tutorial are from [Smashicons](https://www.flaticon.com/authors/smashicons) from [Flaticon](https://www.flaticon.com/).
