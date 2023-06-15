FROM python:3.7.3-stretch

RUN mkdir -p /get_info_app
WORKDIR /get_info_app

ADD ./src/ /get_info_app/
RUN pip install -r requirements.txt
ENV PYTHONPATH=get_info.py

CMD ["python", "get_info.py"]