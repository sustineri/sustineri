FROM python:3.7

LABEL maintainer="hello@mazzotta.me"

# basics
WORKDIR /sustineri/app
COPY app /sustineri
COPY .env /sustineri/app

# prerequisites
RUN apt-get update && apt-get install -qy \
        build-essential \
        libpoppler-cpp-dev \
        pkg-config \
        python-dev && \
    rm -rf /var/lib/apt/lists/*

# python dependencies
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /sustineri/:/sustineri/app/:$PYTHONPATH

EXPOSE 3000

CMD ["python", "index.py"]
