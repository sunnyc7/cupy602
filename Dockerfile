FROM alpine:3.5
RUN apk add --update python py-pip openssl ca-certificates 
RUN pip install pip --upgrade
COPY requirements.txt /src/requirements.txt
RUN apk --update add --virtual build-dependencies python-dev build-base wget \
    && pip install -r /src/requirements.txt \
COPY app.py /src
COPY trader /src/trader
CMD python /src/app.py