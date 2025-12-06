import json

url = "https://api.replicate.com/v1/models/google/imagen-4/predictions"

headers = {
    "Authorization" : f"Bearer {op('base_settings').par.Apikey.eval()}",
    "Content-Type" : "application/json",
    "Prefer" : "wait"
    }

request_body = {
    "input": {
        "prompt": op('text_prompt').text,
        "aspect_ratio": "16:9",
        "output_format": "jpg",
        "safety_filter_level": "block_medium_and_above"
    }
}

op('webclient2').request(url, 'POST', header=headers, data=json.dumps(request_body))
op('switch1').par.index = 1