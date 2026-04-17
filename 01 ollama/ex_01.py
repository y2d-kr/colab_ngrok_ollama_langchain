# 올라마 파이썬 라이브러리 사용해 보기

import os
import ollama

#
# windows 11, PowerShell에서 실행할 때는 다음과 같이 환경변수를 설정해야 합니다.
# ollama의 API 엔드포인트가 https://prorate-mumbo-duty.ngrok-free.dev 라고 가정합니다.
#
# $env:OLLAMA_HOST="https://prorate-mumbo-duty.ngrok-free.dev"
#

result = ollama.generate(
    model="qwen3.5",
    prompt="왜 하늘은 파랗죠?"
)

print(result["response"])
