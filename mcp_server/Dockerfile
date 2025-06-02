# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.11-alpine

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . /app

WORKDIR /app

# Expose application port
EXPOSE 8000

CMD ["python", "mcp_server.py"]
#CMD ["mcp", "run", "mcp_server.py", "--transport", "sse"]