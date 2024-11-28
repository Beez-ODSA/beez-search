FROM python:3.9-slim

WORKDIR /app

# Copy project files
COPY . /app

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Default command to run pytest
CMD ["pytest"]