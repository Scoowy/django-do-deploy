FROM python:3.11.2

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN mkdir /fuzzysystem
COPY . /fuzzysystem
WORKDIR /fuzzysystem
RUN pip3 install -r requirements.txt

RUN chmod +x /fuzzysystem/entrypoint.sh
RUN chmod -R 777 media/

VOLUME /fuzzysystem

EXPOSE 8000

ENTRYPOINT ["sh", "/fuzzysystem/entrypoint.sh"]  # eksekusi bash file entrypoint