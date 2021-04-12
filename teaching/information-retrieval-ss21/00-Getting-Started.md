# Information Retrieval Lab: Getting Started

The lab consists of eight exercises. The first two are meant to give you an introduction to the Python programming language and the Jupyter environment. 
We don't expect you to already know Python, but we will assume some programming experience.

The main part of the lab are exercise 2 through 8, which will be given out in two week intervals. Here, each exercise will implement one component of a basic text search engine:

1. Text Analysis - preprocessing text so that it can be indexed in our search engine.
2. Indexing - programming an index data structure and calculating term statistics.
3. Basic Retrieval - the basic TF/IDF retrieval model.
4. Advanced Retrieval - the Dirichlet Language Model for retrieval
5. Evaluation - evaluating a search engines' performance.
6. Applications - how to scrape web data and index it in a high-performance search framework

## Exercise Format

Each exercise is given as a Jupyter notebook. In case of dependencies or data, we will distribute them alongside the notebook in a folder, so you can easily import them.

Each exercise will also include a reference implementation of the previous exercises, so if at some point you cannot solve an exercise, you can still keep working on the next one!

## Setup

To work on the exercises, you need to have a Jupyter environment up and running.

###### Conda

A simple way of managing a Python environment is Conda, which works across all platforms. You can follow the [official instructions](https://docs.anaconda.com/anaconda/install/) to get Conda running on your computer.
You can then start Jupyter from the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/).
###### Docker
You can run Jupyter from a Docker image that comes with all dependencies included. If you do not have Docker installed, check the [Docker website](https://docs.docker.com/get-docker/) for instructions.
```shell
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/minimal-notebook
```

###### Manual Installation (Linux & macOS)

If you prefer to manually manage your Python environment, you can also set up your environment like so:

```shell
python -m venv venv
source venv/bin/activate
pip install jupyter
jupyter notebook
```
