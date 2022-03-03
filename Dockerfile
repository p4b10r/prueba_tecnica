FROM alpine:3.14

RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       python3 \
                       pkgconfig \
                       git \
                       gcc \
                       openldap \
                       libcurl \
                       python3-dev \
                       gpgme-dev \
                       libc-dev \
    && rm -rf /var/cache/apk/*
RUN apk add --update py3-pip 
RUN pip install six --upgrade --ignore-installed six
RUN pip install --upgrade pip && pip install --upgrade setuptools
RUN apk add build-base
WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt


CMD [ "flask", "run","--host","0.0.0.0" ]
