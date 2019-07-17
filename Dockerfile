# Dockerfile
# FROM directive instructing base image to build upon
FROM python:3.5
MAINTAINER nathankirui5@gmail.com
RUN mkdir /mydata
WORKDIR /mydata
COPY . /mydata
RUN pip install -r requirements.txt
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000


# CMD specifcies the command to execute to start the server running.

ENTRYPOINT ["./start.sh"]
# done!