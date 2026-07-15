from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}"
)

logger.add(
    "logs/application.log",
    rotation="10 MB",
    retention="10 days",
    level="DEBUG"
)