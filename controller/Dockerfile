FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 8000

ENV PYTHONPATH=/app:/app/entrypoint:/app/model:$PYTHONPATH

ENV MANIPULATOR_HOST='manipulator'
ENV MANIPULATOR_PORT=5000


ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "error"]
