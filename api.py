from datetime import datetime
from time import strftime

"""
apis containing functions that we all love
"""

__version__ = "0.1.0"

def get_today():
    """
    Return today's date

    :return: today's date
    :rtype: str
    """
    return datetime.now().strftime('%d%m%Y')


