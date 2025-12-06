"""
webclientDAT callbacks
"""
from typing import Dict, Any
import json

response = op('text_output_buffer')


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
    decoded = json.loads(data.decode('utf-8'))
    if decoded.get('output') != None:
        output = decoded.get('output')
        response.text = output[0].get('content')[0].get('text')
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
