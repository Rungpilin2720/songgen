FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create output directory
RUN mkdir -p static/output

# Expose port (Railway will set PORT env var dynamically)
EXPOSE 8000

# Run the application with PORT from environment variable
CMD sh -c "gunicorn --bind 0.0.0.0:\${PORT:-8000} --workers 1 --worker-class sync --timeout 300 wsgi:app" 