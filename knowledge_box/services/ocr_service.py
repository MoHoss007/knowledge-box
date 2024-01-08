import io
import json
import requests
import re


class OCR:
    url_api = "https://api.ocr.space/parse/image"

    def __init__(self, key: str):
        self.key = key

    def img_to_text(self, file_bytes: io.BytesIO) -> str:
        result = requests.post(self.url_api,
                               files={"file": ('image.png', file_bytes.getvalue())},
                               data={"apikey": self.key,
                                     "language": "eng"})

        if result.status_code == 200:
            result = result.content.decode()
            result = json.loads(result)

            parsed_results = result.get("ParsedResults")[0]
            text_detected = parsed_results.get("ParsedText")
            refined_text = re.sub(r'[^a-zA-Z0-9 .,]', '', text_detected)
            return refined_text

        return "Unable to read text from the file"

    def pdf_to_text(self, file_bytes: io.BytesIO) -> str:
        result = requests.post(self.url_api,
                               files={"file": ('document.pdf', file_bytes.getvalue())},
                               data={"apikey": self.key,
                                     "language": "eng"})

        if result.status_code == 200:
            result = result.content.decode()
            result = json.loads(result)

            parsed_results = result.get("ParsedResults")[0]
            text_detected = parsed_results.get("ParsedText")
            refined_text = re.sub(r'[^a-zA-Z0-9 .,]', '', text_detected)
            return refined_text

        return "Unable to read text from the file"

