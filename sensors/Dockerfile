FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

ENV CONTROLLER_URL=http://controller:8000/data

ENTRYPOINT ["python", "app/main.py"]