# Deep Learning in Python - Setup Guide

- *Course*: Big Data and Language Technologies
- *Date*: 04.04.2022

Welcome to the *Big Data and Language Technologies* Seminar. This setup guide is for you to follow along before starting any of the notebook sessions.
It describes how to set up your working environment and install all necessary dependencies to ensure the notebooks can run without error.

The first step is to setup an isolated development environment so you can install python packages without interfering with your system-wide python installation. Several options exist (`venv`, `pyenv`, `poetry`, and `conda`, to name a few), feel free to use the one you like most. 

We will illustrate the process using `venv`, as it is a lightweight and flexible solution to get up and running fast. If you have never used an environment or the CLI before, we alternatively recommend `conda`: an environment manager that comes both with a CLI and GUI interface. Note that you need to adapt the following steps to whatever environment manager you end up using.

**Important Notes:** 
- we expect you to have **Python 3.9** installed and enabled. Check using `python3 --version` to see what you're currently running and upgrade/switch if needed.
- we expect a UNIX-based OS; if you're using Windows, adapt the Shell commands below to their corresponding Windows syntax, or use WSL

###### Setting up an Environment

If using `venv`, follow the [installation instructions](https://docs.python.org/3/library/venv.html):

1. Create a new virtual environment:

```shell
$ python3 -m venv <path-to-env>
```
2. Activate the created environment:

```shell
$ source <path-to-env>/bin/activate
```

###### Installing Dependencies

Once your environment is activated, you can now install dependencies without interfering with other Python installations.
We supply a [`requirements.txt`](https://temir.org/teaching/big-data-and-language-technologies-ss22/requirements.txt) listing all packages used throughout this course. You can use it to replicate our environment on your local machine to follow along. Packages can be installed using the `pip` package manager.

1. Update `pip`

```shell
$ python3 -m pip install --upgrade pip
```
3. Install all dependencies from the `requirements.txt` file

```shell
$ pip install -r requirements.txt
```

###### Starting Jupyter

Each session is constructed as a [Jupyter Notebook](https://jupyter.org) which allows for interactive programming.
Navigate to the root folder of the seminar and start the notebook folder

```shell
$ jupyter lab
```

And thats it! Your browser should've opened automatically with the Jupyter Lab environment. You're all set.


