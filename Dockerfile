FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for Playwright + OpenCV (Debian 13 / Trixie safe)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libatspi2.0-0 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libnss3 \
    libasound2 \
    libxshmfence1 \
    libwayland-server0 \
    libwayland-client0 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libxext6 \
    libxrender1 \
    libxi6 \
    fonts-unifont \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements file
COPY social-intel-agent/requirements.txt .

# Install Python dependencies (includes Playwright)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install playwright

# Install Chromium browser for Playwright
RUN playwright install chromium

# Copy application code
COPY social-intel-agent /app

# Expose backend port
EXPOSE 8001

# API entry point
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8001"]
