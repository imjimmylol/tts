FROM  python:3.7
EXPOSE 9999


ADD . /app

WORKDIR /app

#Using pip:
RUN python -m pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install -y libfftw3-dev
RUN apt-get install -y libsndfile1-dev

WORKDIR /app/tts_online
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:9999 --noreload
