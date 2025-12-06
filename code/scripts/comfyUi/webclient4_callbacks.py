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
    prompt_id = op('base_flux_settings').par.Promptid.eval()

    data = jsonData.get(prompt_id)

    if data != None:
        op('timer2').par.initialize.pulse()
        outputs = data.get('outputs').get('9')
        img_data = outputs.get('images')[0]
        
        img_url = f"http://{op('base_flux_settings').par.Server}:{op('base_flux_settings').par.Port}/view?filename={img_data.get('filename')}&subfolder={img_data.get('subfolder')}&type={img_data.get('type')}"

        op('moviefilein2').par.file = img_url
        # f"http://10.0.1.137:8000/view?filename={img_data.get('filename')}&subfolder={img_data.get('subfolder')}&type={img_data.get('type')}"
        op('base_flux_settings').par.Generating = False

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
