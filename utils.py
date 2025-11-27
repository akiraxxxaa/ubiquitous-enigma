// Updated: 2025-11-27
"""
Utility functions.
"""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(data):
    """Process input data."""
    return data.upper()
