FROM python:3.11.2

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DJANGO_DEBUG=True
ENV DJANGO_SYMANTO_API_KEY=6dd8dcb6acmsh0ae0691ab41c058p119ad5jsnd876ea394d69

RUN mkdir /fuzzysystem
COPY . /fuzzysystem
WORKDIR /fuzzysystem
RUN pip3 install -r requirements.txt

RUN chmod +x /fuzzysystem/entrypoint.sh

VOLUME /fuzzysystem

EXPOSE 8000

ENTRYPOINT ["sh", "/fuzzysystem/entrypoint.sh"]  # eksekusi bash file entrypoint