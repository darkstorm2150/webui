        with gr.Box(visible=is_spaces):
            if(is_spaces and is_shared_ui):
                gr.HTML(f'''
                <div class="gr-prose" style="max-width: 80%">
                    <p>⚛ Automatic1111 Stable Diffusion Protogen x3.4 Web UI | Running model: ProtoGen X3.4</p>
                    <p>You can find more information on <a href="https://civitai.com/models/3666/protogen-x34-photorealism-official-release" style="target=" _blank"="">this model at civitai.com</a></p>
                    <p>By using this space, You agree to the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" style="target=" _blank"="">CreativeML Open RAIL-M License</a></p>     
                    <p> Code by <a href="https://twitter.com/camenduru" style="target=" _blank"="">camenduru</a> </p>
                </div>
                ''')
            elif(is_spaces):
                import torch
                if(not torch.cuda.is_available()):
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                    <p>⚛ Automatic1111 Stable Diffusion Protogen x3.4 Web UI | Running model: ProtoGen X3.4</p>
                    <p>You can find more information on <a href="https://civitai.com/models/3666/protogen-x34-photorealism-official-release" style="target=" _blank"="">this model at civitai.com</a></p>
                    <p>By using this space, You agree to the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" style="target=" _blank"="">CreativeML Open RAIL-M License</a></p>     
                    <p> Code by <a href="https://twitter.com/camenduru" style="target=" _blank"="">camenduru</a> </p>
                </div>
                ''')
                else:
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                    <p>⚛ Automatic1111 Stable Diffusion Protogen x3.4 Web UI | Running model: ProtoGen X3.4</p>
                    <p>You can find more information on <a href="https://civitai.com/models/3666/protogen-x34-photorealism-official-release" style="target=" _blank"="">this model at civitai.com</a></p>
                    <p>By using this space, You agree to the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" style="target=" _blank"="">CreativeML Open RAIL-M License</a></p>     
                    <p> Code by <a href="https://twitter.com/camenduru" style="target=" _blank"="">camenduru</a> </p>
                </div>
                ''')
