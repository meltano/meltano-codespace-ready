# Codespaces Meltano CLI Starter

This project is a starter for Meltano!

## Step 1 ##
Click "Open on Codespaces".
![Open Codespaces](https://github.com/sbalnojan/meltano-codespace-ready/blob/da4f22d17e3dedfaaafea42c89a7176e1e198e52/codespaceOpen.gif)


## Step 2 ## 
Once in Codespaces, notice the little Dragon on the lefthandside. 

Run

`./meltano_tut init` 

This runs a wrapped "meltano init", adding demo data for you to have fun with.

## Step 3 ##

Add your first extractor to get data from CSV:

`meltano add extractor tap-csv`

Then open up the file `meltano.yml` and add the following configuration to your extractor (you'll just need the bit starting with "config").

```
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
```

## Step 4 ##
Let's test the tap by running:

`meltano invoke tap-csv`

## Step 5 ##

Next add a loader to load our data into a local duckdb:

`meltano add loader target-duckdb``

Again add configuration into the `meltano.yml` as follows: 

  loaders:
  - name: target-duckdb
    variant: jwills
    pip_url: target-duckdb~=0.4
    config:
      filepath: output/my.duckdb
      default_target_schema: raw

Then you can do your first EL run by calling: 

`meltano run tap-csv target-duckdb``

Perfect!

## Step 6 ##
To view your data you can use our little helper:

`./meltano_tut select_db`

is going to run a `SELECT * FROM public.raw_customers` on our duckdb.


## Note ## 
Now that you know there are different types of plugins, you can also use the Meltano extension to
add new plugins. So next time, consider just clicking on the dragon on the LHS and select your mapper!


## Step 7 ##

Now add a "mapper" to do slight modifications on the data we're sourcing here.


`meltano add mapper transform-field` (feel free to use the extension!)

 Add a mapping like this inside the `meltano.yml`:

 ```   
 mappings:
    - name: hide-ips
      config:
         transformations:
          - field_id: "ip_address"
            tap_stream_name: "raw_customers"
            type: "HASH"
 ```          
            
Run and view athe data again!

`./meltano_tut select_db`


= Additional next two steps:
1. add a job,
2. add another tap, e.g. carbon itensity. 


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
