"""
webclientDAT callbacks
"""
from typing import Dict, Any
import json


def onConnect(dat: webclientDAT, id: int):
    """
    Called when a connection is established.

    Args:
            dat: The connected Web Client DAT
            id: The request's unique identifier
    """
    return


def onDisconnect(dat: webclientDAT, id: int):
    """
    Called when a connection is disconnected.

    Args:
            dat: The connected Web Client DAT
            id: The request's unique identifier
    """
    return


def onResponse(dat: webclientDAT, statusCode: Dict[str, Any],
               headerDict: Dict[str, str], data: bytes, id: int):
    """
    Called when a response is received.

    Args:
            dat: The connected Web Client DAT
            statusCode: Status code dictionary with 'code' and 'message'
            headerDict: The header of the response from the server formatted as a 
                    dictionary. Only sent once when streaming.
            data: Response data
            id: The request's unique identifier
    """

    jsonData = json.loads(data.decode('utf-8'))
    prompt_id = jsonData.get('prompt_id')
    op('table_id1')[0, 0] = prompt_id
    op('webclient_check_ready1').par.url = f'10.0.1.137:8000/history/{prompt_id}'
    op('timer1').par.start.pulse()

    return


def onError(dat: webclientDAT, id: int, url: str, error: Exception):
    """
    Called when an error occurs.

    Args:
            dat: The connected Web Client DAT
            id: The request's unique identifier
            url: The URL that caused the error
            error: The exception that occurred
    """
    debug(error)
