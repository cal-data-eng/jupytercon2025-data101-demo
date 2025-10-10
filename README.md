# jupytercon2025-data101-demo

This repository contains code from the demo of the talk [Teaching Data Engineering at Scale With Jupyter Notebooks at UC Berkeley](https://jupytercon2025.sched.com/event/28H4W?iframe=no) by Rebecca Dang, Christy Quang, Lisa Yan, Jonathan M. Ferrari, and Michael Ball, presented at [JupyterCon 2025](https://events.linuxfoundation.org/jupytercon/).

## Quick Links

- Slides (TBA)
- Demo adapted from UC Berkeley's [Data 101 Fall 2025 Project 0](https://data101.org/fa24/)

## Workflow for Instructors

This repo is an example of how to create an assignment on Jupyter notebooks where students can write PostgreSQL queries either directly in the notebook using [JupySQL](https://jupysql.ploomber.io/en/latest/quick-start.html) or in a separate `.sql` file, utilizing the [psycopg3](https://www.psycopg.org/psycopg3/docs/) Python module.

Here is a description of the overall steps:

1. Clone the repository onto your computer and install necessary dependencies. Follow the steps in [Installation](#installation) to do this.
2. Modify the master/source notebook located in `src/proj0/teacher/proj0.ipynb`. This master/source notebook will contain all of the problem instructions, public tests, and hidden tests using the [Otter Autograder system](https://otter-grader.readthedocs.io/en/latest/).
3. If you prefer to use the setup where students write their queries in a separate `.sql` file, you will need to modify the `.sql` files under the `src/proj0/teacher/queries/` directory. This will contain the solution `.sql` files and any skeleton code templates you wish to provide to students. For more information on how to format the `.sql` files, read the comment at the top of `src/proj0/teacher/compile_queries.py`.
4. Otherwise, if you prefer the JupySQL setup, you do not need to make any changes to the `queries` directory.
5. Once you have finalized the master/source notebook and the `queries` directory from step 3, you are ready to compile the source code into the starter code which will be provided to students. Follow the steps in [Compiling the assignment for students](#compiling-the-assignment-for-students) to do this.

For a high-level overview of the workflow for both instructors and students, see also: [Tech Stack Diagram](https://docs.google.com/presentation/d/1RYfQEBiqPjoN-9QkETDhhRB0dtYDvQDdKsFKs8Hk2BY/edit?usp=sharing).

## Installation

1. Clone the repository: `git clone git@github.com:phrdang/jupytercon2025-data101-demo.git`
2. Install PostgreSQL (instructions below are for Mac if you have [Homebrew](https://brew.sh) installed):
    1. Install PSQL client: `brew install libpq`
    2. Install PSQL server: `brew install postgresql`
    3. Start PSQL service: `brew services start postgresql`
3. Setup and activate virtual environment, e.g. using [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html):
    1. Create the environment: `conda create --name demo python=3.11`
    2. Activate the environment: `conda activate demo`
    3. Verify Python version: `python --version` should output `Python 3.11.X`
4. Install dependencies: `pip install -r requirements.txt`

## Compiling the assignment for students

1. Navigate to the `proj0` directory: `cd src/proj0`
2. Compile the master Otter Jupyter notebook into the autograder and student notebooks (see also: [Otter docs](https://otter-grader.readthedocs.io/en/latest/otter_assign/usage.html)): `otter assign teacher/proj0.ipynb compiled-assignment/`
3. If you wish to use the setup with separate `.sql` files, compile the starter code `queries/` directory for students:
    1. `cd teacher`
    2. `python3 compile_queries.py`
    3. Copy over the compiled starter code:
        1. Make sure you are still in the `teacher` directory
        2. `cp -r compiled/ ../compiled-assignment/student/queries/`
