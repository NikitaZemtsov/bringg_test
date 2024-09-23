# Track Your Package

## How to start

Before you begin working with this project, make sure you have set up `pre-commit` for code formatting and linting.
If you haven't already installed `pre-commit`, you can do so via pip:
```bash
pip install pre-commit
pre-commit install
```
Next, ensure that pdm is installed by checking its version: `pdm --version`.
or install with:
```bash
pip install pdm
```
Create venv and activate venv:
```bash
pdm venv create
source .venv/bin/activate
```
Install all dependencies with the following command:
```bash
pdm sync
```
Run app:
```bash
uvicorn --reload src.main:app
```
