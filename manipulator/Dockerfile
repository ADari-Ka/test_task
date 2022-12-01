FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 5000

ENV PYTHONPATH=/app:/app/entrypoint:$PYTHONPATH

ENV HOST='0.0.0.0'
ENV PORT=5000

ENTRYPOINT ["python", "app/main.py"]
