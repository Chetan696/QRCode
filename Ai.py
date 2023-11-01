import qrcode
import torch
from PIL import Image  # Corrected PIL import
import qrcode as qr
from transformers import ControlNetModel, StableDiffusionControlNetPipeline  # Corrected imports

controlnet = ControlNetModel.from_pretrained(
    "DionTimmer/controlnet_qrcode-control_v1p_sd15",  # Removed the full URL
    torch_dtype=torch.float16,
)

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
    safety_checker=None,
).to("cuda")

pipe.enable_xformers_memory_efficient_attention()

def genqrcode():
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=16,
        border=0,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img=qr.make_image(fill_color="Black",black_color="white")

    offset=8*16
    w,h=img.size
    w=(w+225+offset)//256*256
    h = (h + 225 + offset) // 256 * 256
    if w>1024:
        raise 


genqrcode("https://www.linkedin.com/in/chetan-gudditi-922b38272/")