FROM python:3.7

MAINTAINER Emanuele Mazzotta hello@mazzotta.me

# basics
RUN mkdir -p /sustineri
COPY app /sustineri/app
WORKDIR /sustineri/app

# python dependencies
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /sustineri/:/sustineri/app/:$PYTHONPATH

EXPOSE 3000

CMD ["python", "index.py"]
