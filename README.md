# paris-hackathon-consultation

This is an example repo with fake data for the Paris hackathon. 

This uses `themefinder` (https://pypi.org/project/themefinder/) to analyse the responses from public consultations (using example data).

## Quickstart
Clone the repo.

Run `pre-commit install` to install pre-commit hooks.

This uses `poetry` for Python package management - use `poetry install` to install packages.


## Example synthetic data
Example synthetic data for an made-up issue of a new nuclear power plant. This can be found in `example_data`


## Running the Jupyter notebook
The Jupyter notebook `themefinder_example.ipynb` analyses synthetic data to find themes from the synthetic data.

Outputs are in the `example_data/outputs` folder.


## Running the Streamlit app

To run the demo Streamlit app - which displays the outputs of the theme analysis:
```
poetry run streamlit run app/home.py
```