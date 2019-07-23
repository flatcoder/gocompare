FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV test
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
