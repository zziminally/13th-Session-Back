FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 생성·설정
RUN mkdir /app
WORKDIR /app

# 필수 패키지 설치
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base


# Python 종속성 설치 (requirements.txt)
RUN apk update && apk add libpq
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache jpeg-dev zlib-dev mariadb-dev
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apk del jpeg-dev zlib-dev

# 컨테이너로 소스 코드 복사
COPY . /app/