FROM python:3.11-alpine

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir gradio
RUN pip install --no-cache-dir smolagents
RUN pip install --no-cache-dir smolagents[mcp]
RUN pip install --no-cache-dir smolagents[litellm]
RUN pip install --no-cache-dir smolagents[CodeAgent]
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "mcp_client_gradio.py"]
