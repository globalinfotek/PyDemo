FROM python:3.6.0

EXPOSE 8401

RUN pip install flask
RUN pip install requests

COPY main.py /
COPY source /source

ARG VERSION=unknown

# Environment Variables
ENV SERVICE_VERSION=$VERSION
ENV PORT=8401

# entrypoint
CMD [ "python3", "./main.py" ]

