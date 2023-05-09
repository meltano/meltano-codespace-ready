FROM meltano/meltano:latest-python3.10

WORKDIR /home/

COPY . .

# To query results.
RUN pip install duckdb

ENV PATH="$PATH:/venv/bin/meltano"

ENV MELTANO_SYS_DIR_ROOT="/home/.meltano"

RUN meltano install extractors
RUN meltano install loaders
RUN meltano install mappers
