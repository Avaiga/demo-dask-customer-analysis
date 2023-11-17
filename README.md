# Demo Dask Customer Analysis

## Usage
- [Usage](#usage)
- [Demo Dask Customer Analysis](#what-is-demo-dask-customer-analysis)
- [Directory Structure](#directory-structure)
- [License](#license)
- [Installation](#installation)
- [Contributing](#contributing)
- [Code of conduct](#code-of-conduct)

## What is Demo Dask Customer Analysis

Taipy is a Python library for creating Business Applications. More information on our
[website](https://www.taipy.io).

[Demo Dask Customer Analysis](https://github.com/Avaiga/demo-dask-customer-analysis) 
focuses on the seamless integration of Dask (for handling out-of-core data) with Taipy, a 
Python library used for pipeline orchestration and scenario management.

### Demo Type
- **Level**: Intermediate
- **Topic**: GUI/Core

## How to run

This demo works with a Python version superior to 3.8. Install the dependencies of the *requirements.txt* and run the *app.ipynb*.

## Introduction

This application covers a data workflow with 4 tasks:

- Data Preprocessing and Customer Scoring

- Read and process a large dataset using Dask: feature Engineering and Segmentation

- Score customers based on purchase behavior.
Segment Analysis: Segment customers into different categories based on scores and other factors.

- Summary Statistics for High-Value Customers
Analyze each customer segment to derive insights.


## Directory Structure


- `src/`: Contains the demo source code.
    - `algos/`
        ├─ `algo.py`: ur existing code with 4 tasks.
    - `data/`
        ├─ `SMALL_amazon_customers_data.csv`: a sample dataset.
    - `app.ipynb`: Jupyter Notebook for running our sample data application.
    - `config.py`: Taipy configuration which models our data workflow.
    - `config.toml`: (Optional) Taipy configuration in TOML made using Taipy Studio.
- `CODE_OF_CONDUCT.md`: Code of conduct for members and contributors of _demo-dask-customer-analysis_.
- `CONTRIBUTING.md`: Instructions to contribute to _demo-dask-customer-analysis_.
- `INSTALLATION.md`: Instructions to install _demo-dask-customer-analysis_.
- `LICENSE`: The Apache 2.0 License.
- `Pipfile`: File used by the Pipenv virtual environment to manage project dependencies.
- `README.md`: Current file.

## License
Copyright 2022 Avaiga Private Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at
[http://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

## Installation

Want to install _Demo Dask Customer Analysis_? Check out our [`INSTALLATION.md`](INSTALLATION.md) file.

## Contributing

Want to help build _Demo Dask Customer Analysis_? Check out our [`CONTRIBUTING.md`](CONTRIBUTING.md) file.

## Code of conduct

Want to be part of the _Demo Dask Customer Analysis_ community? Check out our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) file.