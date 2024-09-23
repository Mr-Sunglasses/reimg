from io import BytesIO

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image

app = FastAPI()


@app.get("/")
async def resize_image(url: str, width: int, height: int):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))

        resized_image = image.resize((width, height))

        img_byte_arr = BytesIO()
        resized_image.save(img_byte_arr, format=image.format)
        img_byte_arr.seek(0)

        return StreamingResponse(
            img_byte_arr, media_type=f"image/{image.format.lower()}"
        )

    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Failed to download the image")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
