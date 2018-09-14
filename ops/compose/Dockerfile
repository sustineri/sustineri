FROM python:3.7-onbuild

MAINTAINER Emanuele Mazzotta hello@mazzotta.me

RUN mkdir -p /usr/src/sustineri/
ADD ../.. /usr/src/sustineri/
WORKDIR /usr/src/sustineri/
ENV PYTHONPATH /usr/src/sustineri/:/usr/src/sustineri/server/:$PYTHONPATH

EXPOSE 3000

CMD ["python", "app/index.py"]
