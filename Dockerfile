FROM alpine:3.7
EXPOSE 3031
VOLUME /public
VOLUME /private
WORKDIR /usr/src/app
RUN apk add --no-cache \
        uwsgi-python3 \
        python3
COPY ./context .
RUN rm -rf public/*
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["./start.sh"]
