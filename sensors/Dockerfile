FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 8080
ENTRYPOINT ["python", "app/main.py"]

ENV CONTRILLER_URL=http://localhost:8080