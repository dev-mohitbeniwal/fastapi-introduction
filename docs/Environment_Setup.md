# Environment Setup For FastAPI

## Basic Requirements

You must have following installed the following

-   Python 3.6+
-   Pip

## Preferred Option

Managing the Python environments using Anaconda is really easy. With conda environment you can use multiple python versions in different virutal environments and the conda CLI helps with a lot of other problems.

### Step 1: Installing Anaconda

-   Download the .dmg file from using this [link](https://repo.anaconda.com/archive/Anaconda3-2023.07-1-MacOSX-arm64.pkg) This is the latest version of Anaconda at present.
-   Install the Anaconda with default configuration.

### Step 2: Managing Virtual Environment

After ensuring you have the conda binary added to your shell path you can proceed with the following steps

#### Creating a new environment

```bash
conda create -n <environment> python=<python_version>
```

E.g.:

```bash
conda create -n fastapi-test python=3.8
```

#### Listing existing environments:

```bash
conda list env
```

#### Activating a specific environment

```bash
conda activate <environment_name>
```

#### Removing conda environment

```bash
conda remove --name <environment_name> --all
```

The `--all` flag removes all the packages installed in that environment.

## Setting up Environment for the FastAPI POC

1. Create new environment:
    ```bash
    conda create -n fastapi-poc python=3.8
    ```
2. Activate environment:
    ```bash
    conda activate fastapi-poc
    ```
3. Installing required packages:
   With conda pip is available in all the environments by default. When you install any package using pip inside an environment, those packages remain isolated within that particular environment.

    With pip you can install multiple packages using requirements file. For this POC you can install all the required packages by running the following command from the root directory of this project:

    ```bash
    pip install -r ./requirements.txt
    ```

### [Next Topic: Getting Started with Fast API](/docs/Getting_Started.md)

### [Previous Topic: Introduction to FastAPI](../ReadMe.md)
