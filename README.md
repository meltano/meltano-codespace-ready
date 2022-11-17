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

## Step 6 ##
View the results :-) 



https://github.com/anelendata/tap-exchangeratehost


- [Bracket Pair ...]()
### Operating System
