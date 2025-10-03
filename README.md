# jupytercon2025-data101-demo

JupyterCon 2025 Data 101 Demo

- [Link to talk](https://jupytercon2025.sched.com/event/28H4W?iframe=no)
- Slides (TBA)
- Demo adapted from [Data 101 Fall 2025 Project 0](https://data101.org/fa24/)

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
3. Compile the starter code `queries/` directory for students:
    1. `cd teacher`
    2. `python3 compile_queries.py`
4. Copy over the compiled starter code:
    1. Make sure you are still in the `teacher` directory
    2. `cp -r compiled/ ../compiled-assignment/student/queries/`

<!-- TODO: had to replace !psql with !opt/homebrew/bin/psql

$ psql -d postgres -U rebeccadang
replace Owner: michael references in billboard.sql to Owner: rebeccadang
TODO: rezip billboard.zip file from billboard.sql file with correct owner?
-->

<!-- TODO: windows instructions?
local jupyterhub instructions?
 -->