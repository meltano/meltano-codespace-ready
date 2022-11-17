# Codespaces Meltano CLI Starter

This project is a starter for ...

## Step 1 ##
Click "Open on Codespaces"

## Step 2 ## 
Once in Codespaces, notice the little Dragon on the lefthandside. That's a useful extension called ...

Click on it, right now your project is empty, so let us get started!

The first step is to init a project by running in the integrated terminal:

`mkdir meltano_project; cd meltano_project`

`meltano init .`

## Step 3 ##

meltano add extractor tap-carbon-intensity

plugins:
  extractors:
  - name: tap-csv
    variant: meltanolabs
    pip_url: git+https://github.com/MeltanoLabs/tap-csv.git
    config:
      files:
      - entity: raw_customers
        path: /workspaces/meltano-codespace-ready/mel_proj/customers.csv
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
      filepath: output/db
      default_target_schema: public

meltano run tap-csv target-duckdb

## Step 6 ##
View the results :-) 



https://github.com/anelendata/tap-exchangeratehost


- [Bracket Pair ...]()
### Operating System
