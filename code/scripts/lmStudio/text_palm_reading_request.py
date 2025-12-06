import json
import base64

client: webclientDAT = op('webclient2')

img_bytes = op('null_img_buffer').saveByteArray('.jpg')
img_data = base64.b64encode(img_bytes).decode('utf-8')

headers = {"Content-Type": "application/json"}
msg = {
    "input": [    
        {
        "role": "user",
        "content": [
            { "type": "input_text", "text": op('text_input1').text },
            {
                "type": "input_image",
                "image_url": f"data:image/jpg;base64,{img_data}",
            },
        ],
        }
    ],
    "model": "qwen/qwen3-vl-8b",
    "reasoning": { "effort": "low" },

}




client.request("http://10.0.1.137:1234/v1/responses",
               "POST", data=json.dumps(msg).encode('utf-8'), header=headers)
