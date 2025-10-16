"""Logging utilities for FastMCP."""

import logging
from typing import Literal


def get_logger(name: str) -> logging.Logger:
    """Get a logger nested under MCPnamespace.

    Args:
        name: the name of the logger, which will be prefixed with 'FastMCP.'

    Returns:
        a configured logger instance
    """
    return logging.getLogger(name)


def configure_logging(
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO",
) -> None:
    """Configure logging for MCP.

    Args:
        level: the log level to use
    """
    handlers: list[logging.Handler] = []
    try:
        from rich.console import Console
        from rich.logging import RichHandler

        handlers.append(RichHandler(console=Console(stderr=True), rich_tracebacks=True))
    except ImportError:
        pass

    if not handlers:
        handlers.append(logging.StreamHandler())

    formatter = logging.Formatter("%(message)s")

    logger = logging.getLogger("mcp")
    logger.setLevel(level)
    logger.propagate = False
    
    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.info("Logging configured")