import json

client: webclientDAT = op('webclient1')

headers = {"Content-Type": "application/json"}
msg = {
    "input": op('text_input').text,
    "model": "qwen/qwen3-vl-8b",
}

client.request("http://10.0.1.137:1234/v1/responses",
               "POST", data=json.dumps(msg).encode('utf-8'), header=headers)
