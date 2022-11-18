# Codespaces Meltano CLI Starter

This project is a starter for ...

## Step 1 ##
Click "Open on Codespaces"

## Step 2 ## 
Once in Codespaces, notice the little Dragon on the lefthandside. 

`./meltano_tut init` 

This runs a wrapped "meltano init", adding demo data to have fun with.

## Step 3 ##

meltano add extractor tap-csv

plugins:
  extractors:
  - name: tap-csv
    variant: meltanolabs
    pip_url: git+https://github.com/MeltanoLabs/tap-csv.git
    config:
      files:
      - entity: raw_customers
        path: data/customers.csv
        keys: [id]


## Step 4 ##
meltano invoke tap-csv

## Step 5 ##

meltano add loader target-duckdb

  loaders:
  - name: target-duckdb
    variant: jwills
    pip_url: target-duckdb~=0.4
    config:
      filepath: output/my.duckdb
      default_target_schema: raw

meltano run tap-csv target-duckdb

## Step 5b ## 
Now that you know there are different types of plugins, you can also use the Meltano extension to
add new plugins. So next time, consider just clicking on the dragon on the LHS and select your mapper!

## Step 6 ##
./meltano_tut select_db


## Step 7 ##

 meltano add mapper transform-field
 
 Add a mapping like this:
 ```   
 mappings:
    - name: hide-ips
      config:
         transformations:
          - field_id: "ip_address"
            tap_stream_name: "raw_customers"
            type: "HASH"
 ```          
            
Run and view again!!

=== Use Utility to add tap-carbonintensity or sth similar, and then be done...


== Add a "job", done.


===


====== Tutorial Done ====


## Step 8 ##

meltano add transformer dbt-duckdb

```
  transformers:
  - name: dbt-duckdb
    variant: jwills
    pip_url: dbt-core~=1.2.0 dbt-duckdb~=1.2.0
    config:
      path: 'output/my.duckdb'
      schema: analytics 
```

into transform/models/raw/sources.yml

```
config-version: 2
version: 2
sources:
  - name: raw     # the name we want to reference this source by
    schema: raw   # the schema the raw data was loaded into
    tables:
      - name: customers
```

## Step 9 ##

into transform/models/raw/customers.sql

````
{{
  config(
    materialized='table'
  )
}}


with base as (select *
from {{ source('raw', 'customers') }}) 

select id, first_name, last_name
```

then 
`meltano invoke dbt-duckdb:run``
version: 
