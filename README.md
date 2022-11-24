# Codespaces Meltano CLI Starter
Have your *first meltano pipeline run within 5 minutes* using this repository, even if you never touched [Meltano](https://github.com/meltano) before.

No install needed, just a GitHub account (and a few spare Codespaces minutes you get for free anways).

Let's get started!

## Step 1 ##
Click "Open on Codespaces", to launch this project into a ready to use web VS-Code version with everything preloaded.


![Open Codespaces](https://github.com/sbalnojan/meltano-codespace-ready/blob/da4f22d17e3dedfaaafea42c89a7176e1e198e52/codespaceOpen.gif)

**Make sure to open up the README.md inside Codespaces as well.**

## Step 2 - from inside Codespaces ## 
Inside the terminal (bottom window) run 

`./meltano_tut init` 

This runs a wrapped "meltano init", adding demo data for you to have fun with.

You can take a look around:
- there is a file "data/customers.csv", it is the one you will be loading into a datawarehouse.
- there are now a bunch of Meltano project files, including the important "meltano.yml"

## Step 3  - add your first extractor ##

Add your first extractor to get data from the CSV. Do so by running inside the terminal:

`meltano add extractor tap-csv`

Then open up the file `meltano.yml` and add the following configuration to your extractor (you'll just need the bit starting with "config").

```
plugins:
  extractors:
  - name: tap-csv
    variant: meltanolabs
    pip_url: git+https://github.com/MeltanoLabs/tap-csv.git
    config:                                                 #<<--- You just need the part starting here!
      files:
      - entity: raw_customers
        path: data/customers.csv
        keys: [id]
```

## Step 4 Test run your tap##


Let's test the tap by running:

`meltano invoke tap-csv`

If everything works as expected, Meltano should extract the CSV and dump it as a "stream" onto standard output inside the terminal.

## Step 5 Add a loader ##

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

Then you can do your first complete EL run by calling: 

`meltano run tap-csv target-duckdb``

Perfect!

## Step 6 View the loaded data ##
To view your data you can use our little helper:

`./meltano_tut select_db`

is going to run a `SELECT * FROM public.raw_customers` on our duckdb, and write the output to the terminal.

Great! You've completed your first extract and load run.

## Step 7 remover the plain text ip adresses ##

Notice that the data you just viewed had plain IP adresses inside of it? As a last thing,
let us take care of that. 

Add a "mapper" to do slight modifications on the data we're sourcing here.

`meltano add mapper transform-field`

 Then head over to the `meltano.yml`file and add a mapping like this just below the new plugin.

 ```
   - name: transform-field
    variant: transferwise
    pip_url: pipelinewise-transform-field
    executable: transform-field
    mappings:
      - name: hide-ips
        config:
           transformations:
            - field_id: "ip_address"
              tap_stream_name: "raw_customers"
              type: "HASH"
 ```          
            
Run and view the data again!

`./meltano_tut select_db`

## Step 8 celebrate your success ##

That was fun and quick! Now try to run 
`meltano draon` 

just for the fun of it ;)

More things you can explore inside this codespace: 
- Do you see the little dragon on the left hand side? That's the Meltano VS Code extension. It allows you to view and add all possible taps & targets we currently have on the Meltano hub. Take a look at them!
- Why don't you try to add a second output? Try to add the "target-jsonl" and do a "meltano run tap-csv target-jsonl".
- Next, try to add another tap, for instance the "tap-carbon-intensity", play around with it and push the data into either target.

Once you're done, head over to the docs and check out our [great getting started tutorial](https://docs.meltano.com/) for more details, add a job and schedule to your extract & load processes, and deploy it to production.
