FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY . /src/app
WORKDIR /src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

ENTRYPOINT ["/src/app/run.sh"]