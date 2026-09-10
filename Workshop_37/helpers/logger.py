import logging
from pathlib import Path


# Create logs folder
log_folder = Path(__file__).parent.parent / "logs"
log_folder.mkdir(exist_ok=True)

# Log file
log_file = log_folder / "test.log"


# Logging configuration
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Create logger
logger = logging.getLogger(__name__)