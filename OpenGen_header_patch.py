        with gr.Box(visible=is_spaces):
            if(is_spaces and is_shared_ui):
                gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                    <p>This is currently running OpenGen V1 a continuation of the Protogen Model for Stable Diffusion</p>
                    <p>This Web-UI is Under Development, crashes may occur</a></p>
                    <p>By using this space, You agree to the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" style="target=" _blank"="">CreativeML Open RAIL-M License</a></p>
                    <p>Opengen A10G Large demo</a></p>
                    <p> Code by <a href="https://twitter.com/camenduru" style="target=" _blank"="">camenduru</a> </p>
                </div>
                ''')
            elif(is_spaces):
                import torch
                if(not torch.cuda.is_available()):
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                    <p>This is currently running OpenGen V1 a continuation of the Protogen Model for Stable Diffusion</p>
                    <p>This Web-UI is Under Development, crashes may occur</a></p>
                    <p>By using this space, You agree to the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" style="target=" _blank"="">CreativeML Open RAIL-M License</a></p>
                    <p>Opengen A10G Large demo</a></p>
                    <p> Code by <a href="https://twitter.com/camenduru" style="target=" _blank"="">camenduru</a> </p>
                </div>
                ''')
                else:
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                    <p>This is currently running OpenGen V1 a continuation of the Protogen Model for Stable Diffusion</p>
                    <p>This Web-UI is Under Development, crashes may occur</a></p>
                    <p>By using this space, You agree to the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" style="target=" _blank"="">CreativeML Open RAIL-M License</a></p>
                    <p>Opengen A10G Large demo</a></p>
                    <p> Code by <a href="https://twitter.com/camenduru" style="target=" _blank"="">camenduru</a> </p>
                </div>
                ''')
