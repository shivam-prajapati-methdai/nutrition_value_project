from PIL import Image
import numpy as np
import io
import re
import base64

def run_inference(raw_data):
    img_b64 = re.sub('^data:image/.+;base64,', '', raw_data)
    img_bytes = base64.b64decode(img_b64)
    img = Image.open(io.BytesIO(img_bytes)).resize([228, 228]).convert("RGB")
    img = np.array(img).astype(np.float32) / 255.0
    
    # res = model.predict(np.expand_dims(img, axis = 0))
    # res = np.argmax(res)
    
    return "processed"