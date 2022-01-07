FROM  python:3.7
EXPOSE 9998


ADD . /app

WORKDIR /app

#Using pip:
RUN python -m pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install -y libfftw3-dev
RUN apt-get install -y libsndfile1-dev
RUN apt-get install -y iputils-ping
RUN pip install git+https://github.com/repodiac/german_transliterate

# WORKDIR /app/tts_online

# CMD ping 127.0.0.1

RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:9998
