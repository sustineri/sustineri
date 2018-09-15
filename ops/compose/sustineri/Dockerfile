FROM python:3.7

MAINTAINER Emanuele Mazzotta hello@mazzotta.me

# basics
RUN mkdir -p /sustineri
COPY app /sustineri/app
COPY .env /sustineri/app/.env
WORKDIR /sustineri/app

# prerequisites
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    python-dev

# python dependencies
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /sustineri/:/sustineri/app/:$PYTHONPATH

EXPOSE 3000

CMD ["python", "index.py"]
