FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 5000

ENV PYTHONPATH=/app:/app/entrypoint:$PYTHONPATH

ENV CONTROLLER_HOST='controller'
ENV CONTROLLER_PORT=8000


ENTRYPOINT ["python", "app/main.py"]
