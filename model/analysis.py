from model.model_classes.solar_data import SolarData


def run_analysis(filepath: str) -> None:
    solar_data = SolarData(filepath)