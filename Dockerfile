FROM bitnami/spark:3.4.1

USER root

RUN install_packages python3 curl && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3 && \
    pip install --no-cache-dir requests

USER 1001

COPY ./src /opt/bitnami/spark-apps/

ENV PYSPARK_PYTHON=python3

RUN python3 -m pip install --no-cache-dir python-dotenv

CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1", "/opt/bitnami/spark-apps/main.py"]
# CMD [ "tail", "-f", "/dev/null" ]
