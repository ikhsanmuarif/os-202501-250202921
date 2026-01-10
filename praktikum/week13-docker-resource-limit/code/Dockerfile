# Base image: Python slim untuk ukuran lebih kecil
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy aplikasi ke container
COPY app.py .

# Buat executable
RUN chmod +x app.py

# Label metadata
LABEL maintainer="student@example.com"
LABEL description="Docker Resource Limit Test Application"
LABEL version="1.0"

# Command untuk menjalankan aplikasi
CMD ["python3", "app.py"]
