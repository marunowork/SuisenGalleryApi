FROM python:3.6

WORKDIR /app 

RUN pip install flask
RUN pip install flask_cors
RUN pip install requests_html
RUN pip install instagram-scraper
COPY galleryapi.py ./app/
COPY constants.py ./app/
COPY jsonp_flask.py ./app/

CMD ["python", "galleryapi.py"]
