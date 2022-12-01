FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 8080
ENTRYPOINT ["python", "app/main.py"]

ENV CONTROLLER_URI=http://controller:8000