FROM python:3.8.3-alpine

RUN mkdir -p /app
WORKDIR /app

ADD ./src/ /app/
RUN pip install -r requirements.txt
ENV PYTHONPATH=get_info.py

CMD ["python", "get_info.py"]