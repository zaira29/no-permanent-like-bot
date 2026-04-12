FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py.

ENV BOT TOKEN=
"8630175808:AAF2HxYop3A0jjHo7HHmc6s05hhs9SDm4DA"
ENV API_URL_TEMPLATE=""
ENV WEBHOOK_URL="https://no-permanent-like-bot.onrender.com/"
ENV PORT=5000
ENV TZ-Asia/Kolkata
RUN In -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["python", "bot.py"]