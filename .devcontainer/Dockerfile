FROM meltano/meltano:v2.9.0-python3.10

WORKDIR /home/

COPY . .

#RUN bash ./setup.sh

# To query results.
RUN pip install duckdb
ENV PATH="$PATH:/venv/bin/meltano"
