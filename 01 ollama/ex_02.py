# 올라마 파이썬 라이브러리 사용해 보기
# Chat API로 대화 주고받기

import os
import ollama

#
# windows 11, PowerShell에서 실행할 때는 다음과 같이 환경변수를 설정해야 합니다.
# ollama의 API 엔드포인트가 https://prorate-mumbo-duty.ngrok-free.dev 라고 가정합니다.
#
# $env:OLLAMA_HOST="https://prorate-mumbo-duty.ngrok-free.dev"
#

conversation = [
    {"role": "system", "content": "당신은 까칠한 10대입니다."},
    {"role": "user", "content": "안녕, 오늘 기분 어때?"}
]

reply = ollama.chat(
    model="qwen3.5",
    messages=conversation
)

print(reply.message.content)
