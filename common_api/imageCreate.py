import os

from django.http import JsonResponse
from fastapi import FastAPI
from openai import OpenAI
import logging
import json
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 핸들러 설정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 핸들러 추가
logger.addHandler(console_handler)

app = FastAPI()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

@csrf_exempt
def ai_image_create(request):
    data = json.loads(request.body)

    response = client.images.generate(
        model="dall-e-3",
        prompt=data.get("prompt"),
        size="1024x1024",
        quality="standard",
    )

    logger.info(response.data[0].url)

    return JsonResponse(response.data[0].url, safe=False)