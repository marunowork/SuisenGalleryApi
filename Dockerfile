FROM python:3.6

WORKDIR /app 

RUN pip install flask
RUN pip install flask_cors
RUN pip install requests_html
RUN pip install instagram-scraper

CMD ["python", "galleryapi.py"]
