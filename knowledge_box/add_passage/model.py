import io
import json
import cv2
import numpy as np
import requests


class OCR:
    url_api = "https://api.ocr.space/parse/image"

    def __init__(self):
        with open(r'knowledge_box/add_passage/key.json', 'r') as file:
            data = json.load(file)
        self.key = data["apikey"]

    def image_to_text(self, img: np.array) -> str:
        _, compressedimage = cv2.imencode(".jpg", img, [1, 90])
        file_bytes = io.BytesIO(compressedimage)

        result = requests.post(self.url_api,
                               files={"creenshot 2023-11-04 181457.png": file_bytes},
                               data={"apikey": self.key,
                                     "language": "eng"})

        result = result.content.decode()
        result = json.loads(result)

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")
        return text_detected
