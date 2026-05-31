# Sử dụng bản slim để giảm dung lượng image
FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các gói hệ thống cần thiết (nếu có thư viện yêu cầu compile)
# Ở đây cài thêm tzdata để xử lý múi giờ
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Sao chép và cài đặt dependencies trước để tận dụng Docker Layer Caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Thiết lập biến môi trường
ENV TZ=Asia/Ho_Chi_Minh
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Các biến này bạn có thể set trực tiếp trên Dashboard của Render 
# (Environment Variables) để bảo mật hơn, nhưng nếu muốn để đây thì:
ENV BOT_TOKEN="8701172834:AAHiFRflATS1Z8uKv-a7EBL9dx4eFhhI65M"
ENV WEBHOOK_URL="https://no-permanent-like-bot-uooc.onrender.com"
ENV PORT=10000

# Thiết lập múi giờ
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Chạy bot
CMD ["python", "bot.py"]
