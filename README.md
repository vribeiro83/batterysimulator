# Battery Simulator
With the Netherlands moving away from Net-Metering, this Battery Simulator is a playful, entertaining, and learning, attempt to estimates, based on previous usage, what might be thre ROI of investing on a Battery.

This is for entertainment purposes, you should do your own due deligence.

## Requirements
- Python 3.12 or higher
- Poetry (https://python-poetry.org/)

## Installation

Install dependencies with Poetry:

```bash
pip install poetry
poetry install
```

## Running the code
You require to input a csv file, this at the moment has been tested on output from Ephanse app. Run the code below with the full path to the file:

```bash
python main.py --csv path_to_file.csv
```