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

<!-- TODO: had to replace !psql with !opt/homebrew/bin/psql

$ psql -d postgres -U rebeccadang
replace Owner: michael references in billboard.sql to Owner: rebeccadang
TODO: rezip billboard.zip file from billboard.sql file with correct owner?
-->

<!-- TODO: windows instructions?
local jupyterhub instructions?
 -->