# Team Name: DreamTeam2006

## Team Members

    Nyiri Szabolcs Balázs - REMAIO
    Pap Arion - YJWQMP

## Project Description

The goal of this project is to gather you own real-world image dataset with different types of objects in it and train an image classifier for solving it. Dataset examples: books vs shoes vs furniture, houseplants vs outdoor plants vs trees. Make sure that your dataset contains at least 3 classes, with at least 50 examples each (1 image per object). Make sure that the gathered images are diverse, with varied view angles, background and lighting. Select classes such that the task is not trivial to solve.

The main difficulty in this task will be the small dataset size, think through what we learned in class for solving it. Build an image classification pipeline for your dataset and train multiple networks on it, compare their performance. Inspect failure cases.

## Function of Files

dockerfile: Building and running the docker container

requirements.txt: Contains the required package names and versions

ReadMe: Containts documentation

main.ipynb: Containts the code of the project

## Related Works

Related GitHub repository: <https://lightning.ai/docs/pytorch/stable/notebooks/lightning_examples/cifar10-baseline.html>

Related paper: <https://arxiv.org/abs/1512.03385>

## How to run

Build with: `docker build -t mt-hf-notebook .`

Run with: `docker run -it -p 8888:8888 mt-hf-notebook`

Three links will be given, choose the link starting with: "<http://127.0.0.1:8888/tree?token=>..."

In the browser you will see a directory, choose `main.ipynb`

In there you can start running the code cell-by-cell

Running the pipline: run the code cell-by-cell

Running the models: There are two models, one random choosing and one basic neural network.
You will find these by the header texts. First define the models, then run the prediction or fit the model and then predict.

Running the Evaluation: After every model prediction, there is an evaluation step in the same cell that displays the results.
