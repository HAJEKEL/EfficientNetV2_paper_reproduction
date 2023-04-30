# DARTS Search Reproduction

This repository contains instructions for reproducing the DARTS (Differentiable Architecture Search) search with a google colab [ipynb file](https://github.com/HAJEKEL/EfficientNetV2_paper_reproduction/blob/main/darts_search.ipynb) running on a Google Compute Engine (GCE) virtual machine instance with a GPU. The DARTS source code can be found in the [pt.darts](https://github.com/HAJEKEL/pt.darts/tree/darts_efficient_mobilenet) repo. 

## Prerequisites

Before starting the DARTS search reproduction, make sure you have the following:

- A Google Cloud Platform (GCP) account.
- A Google Compute Engine (GCE) project with GPU quota in all regions.
- Basic knowledge of using GCE instances and connecting to them from a Jupyter notebook.


## Reproduction Steps

To reproduce the DARTS search, follow the steps below:

1. Create a Google Compute Engine virtual machine instance with at least one GPU in all regions. You can follow the steps below:
   - Go to the [GCP Console](https://console.cloud.google.com/) and create a new project if you haven't done so already.
   - Go to the **IAM & admin > Quotas** page and search for "gpus_all_regions".
   - Select the "GPUs (all regions)" quota and click **Edit Quotas**. Apply for at least 1 GPU in all regions. You can use **fast.ai** as description for the quota application.
   - Wait untill you get a conformation in you mailbox. 
2. Launch a Google Colab virtual machine instance with a GPU:
   - Search for "Colab Marketplace" and click on the first result.
   - Deploy the VM with your desired configuration, the standard given one is fine. 
   - If there are no available VM instances in your current region, iterate through different zones until you find one with available instances.
3. Connect your Google Colab runtime to the GCE instance:
   - Copy the [ipynb file](https://github.com/HAJEKEL/EfficientNetV2_paper_reproduction/blob/main/darts_search.ipynb) in google drive. Open it with google colab, click on "Connect to a custom GCE VM".
   - Add the GCE project ID, zone of the VM, and the VM instance name.
4. Follow the steps inside the [ipynb file](https://github.com/HAJEKEL/EfficientNetV2_paper_reproduction/blob/main/darts_search.ipynb):
   - Comments inside the file explain what's going on. 
   - Note that the source code allows for training on 3 different datasets, MNIST, fashionMNIST and CIFAR10. Options for the search such as which dataset and the number of epochs, are defined in [config.py](https://github.com/HAJEKEL/pt.darts/blob/master/config.py).

## Darts algoritm

The DARTS source code can be found in the [pt.darts](https://github.com/HAJEKEL/pt.darts/tree/darts_efficient_mobilenet) repo. The README there will guide you through the source code. 