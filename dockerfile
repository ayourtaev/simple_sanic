FROM ubuntu:latest
MAINTAINER igloo
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python-dev python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r req.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
