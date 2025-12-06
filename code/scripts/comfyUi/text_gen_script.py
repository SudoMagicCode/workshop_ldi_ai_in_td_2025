import json
import comfyRequest
webClient = op('webclient_gen_img2')




url = f"{op('base_flux_settings').par.Server}:{op('base_flux_settings').par.Port}/prompt"

prompt:dict = comfyRequest.build_prompt(
    width=512, height=512, seed=absTime.frame, steps=20, promptText=op('text_prompt_text').text)

msg = {"prompt": prompt, "client_id": "3376"}
data = json.dumps(msg).encode('utf-8')
headers = headers = {"Content-Type": "application/json"}


op('base_flux_settings').par.Generating = 1
webClient.request(url, "POST", data=data, header=headers)
