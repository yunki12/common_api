import os

from django.http import JsonResponse, HttpResponse
from fastapi import FastAPI
from openai import OpenAI
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 핸들러 설정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 포매터 설정
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 핸들러 추가
logger.addHandler(console_handler)

app = FastAPI()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def book_recommend(request):
    # 현재 날짜와 시간 가져오기
    current_date = datetime.now()

    # 형식 지정 (예: "2025년 03월 22일")
    formatted_date = current_date.strftime("%Y년 %m월 %d일")
    logger.info("형식 지정된 날짜:")
    logger.info(formatted_date)

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '당신은 도서 추천을 위해 훈련된 고도로 숙련된 AI 입니다."'},
            {'role': 'user', 'content': f"{formatted_date} 기준 으로 한국에서 최신 인기 있는 도서 추천 해줘"},
        ],
        temperature=0
    )

    logger.info(response)

    return JsonResponse(response.choices[0].message.content, safe=False)
    #return JsonResponse({}, safe=False)