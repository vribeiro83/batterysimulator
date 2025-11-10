import logging

def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure global logging for the project.
    Should be called once in main.py before other imports.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
