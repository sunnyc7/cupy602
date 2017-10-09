FROM alpine:3.5
RUN apk add --update python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install pip --upgrade
RUN pip install --trusted-host pypi.python.org -r /src/requirements.txt
COPY app.py /src
COPY trader /src/trader
CMD python /src/app.py