        with gr.Box(visible=is_spaces):
            if(is_spaces and is_shared_ui):
                gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
            <p>Currently, this platform is operating on OpenGen V1, which is an extension of the Protogen Model, specifically designed for Stable Diffusion.</p>
            <p>Please note that our Web User Interface is still in the development phase. Hence, occasional system crashes may be expected.</p>
            <p>By interacting within this environment, you hereby acknowledge and agree to the terms of the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" target="_blank">CreativeML Open RAIL-M License</a>.</p>
            <p>Here we present a large-scale demonstration of OpenGen A10G.</p>
            <p>The underlying code was created by <a href="https://twitter.com/camenduru" target="_blank">Camenduru</a>.</p>
            </div>
                ''')
            elif(is_spaces):
                import torch
                if(not torch.cuda.is_available()):
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
            <p>Currently, this platform is operating on OpenGen V1, which is an extension of the Protogen Model, specifically designed for Stable Diffusion.</p>
            <p>Please note that our Web User Interface is still in the development phase. Hence, occasional system crashes may be expected.</p>
            <p>By interacting within this environment, you hereby acknowledge and agree to the terms of the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" target="_blank">CreativeML Open RAIL-M License</a>.</p>
            <p>Here we present a large-scale demonstration of OpenGen A10G.</p>
            <p>The underlying code was created by <a href="https://twitter.com/camenduru" target="_blank">Camenduru</a>.</p>
            </div>
                ''')
                else:
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
            <p>Currently, this platform is operating on OpenGen V1, which is an extension of the Protogen Model, specifically designed for Stable Diffusion.</p>
            <p>Please note that our Web User Interface is still in the development phase. Hence, occasional system crashes may be expected.</p>
            <p>By interacting within this environment, you hereby acknowledge and agree to the terms of the <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license" target="_blank">CreativeML Open RAIL-M License</a>.</p>
            <p>Here we present a large-scale demonstration of OpenGen A10G.</p>
            <p>The underlying code was created by <a href="https://twitter.com/camenduru" target="_blank">Camenduru</a>.</p>
            </div>
                ''')
