# Codespaces Meltano CLI Starter
Have your *first meltano pipeline run within 5 minutes* using this repository, even if you never touched [Meltano](https://github.com/meltano) before.

No install needed, just a GitHub account (and a few spare Codespaces minutes you get for free anyways).

Let's get started!

## Step 0 - Open Codespaces

*If you opened this from our homepage, you can go straight to Step 1.*

Click "Open on Codespaces", to launch this project into a ready to use web VS-Code version with everything preloaded.

![Open Codespaces](codespaceOpen.gif)

**Make sure to open up the README.md inside Codespaces as well.**

*Notes on codespaces:* 
- If you at any point get an error "The user denied permission to use Service Worker", then you need to enable third-party cookies. [It's a codespaces related problem](https://github.com/orgs/community/discussions/26316).
- In our experience, codespaces work best in Chrome or Firefox, not so well in Safari.
- Files in codespaces autosave! No need to save anything.

## Step 1 - Initialize Meltano Project

Inside the terminal (bottom window) run: 

> `./meltano_tut init` 

This runs a wrapped "meltano init", adding demo data for you to have fun with.

You can take a look around:
- there is a file "data/customers.csv", it is the one you will be loading into a datawarehouse.
- there are now a bunch of Meltano project files, including the important "meltano.yml"

## Step 2  - Add your first extractor

Add your first extractor to get data from the CSV. Do so by running inside the terminal:

> `meltano add extractor tap-csv`

Then open up the file `meltano.yml`, copy the config below, and paste it below `pip_url`.

```yaml
    config:
      files:
      - entity: raw_customers
        path: data/customers.csv
        keys: [id]
```

Your config for tap-csv in `meltano.yml` should look like this:

```yaml
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

## Step 3 - Test run your tap

Let's test the tap by running:

> `meltano invoke tap-csv`

If everything works as expected, Meltano should extract the CSV and dump it as a "stream" onto standard output inside the terminal.

## Step 4 - Add a loader

Next add a loader to load our data into a local duckdb:

> `meltano add loader target-duckdb`

Copy the configuration below and paste it below the `pip_url` for target-duckdb in the `meltano.yml` file.

```yaml
    config:
      filepath: output/my.duckdb
      default_target_schema: raw
```

The config in `meltano.yml` for target-duckdb should look like this:

```yaml
  loaders:
  - name: target-duckdb
    variant: jwills
    pip_url: target-duckdb~=0.4
    config:
      filepath: output/my.duckdb
      default_target_schema: raw
```

## Step 5 - Run your EL pipeline

Now you can do your first complete EL run by calling `meltano run`! 

> `meltano run tap-csv target-duckdb`

Perfect!

## Step 6 - View loaded data

To view your data you can use our little helper:

> `./meltano_tut select_db`

This will run a `SELECT * FROM public.raw_customers` on your duckdb instance and write the output to the terminal.

Great! You've completed your first extract and load run. 🥳

## Step 7 - Remove plain text IP adresses

Notice that the data you just viewed had plain IP adresses inside of it? Let's quickly get rid of those!

Add a "mapper" to do slight modifications on the data we're sourcing here.

> `meltano add mapper transform-field`

 Then paste the following config below the `pip_url` for the `transform-field` mapper in your `meltano.yml` file.

```yaml
    mappings:
    - name: hide-ips
      config:
         transformations:
         - field_id: "ip_address"
           tap_stream_name: "raw_customers"
           type: "HASH"
```

The full configuration for the mapper `transform-field` should look like this:

 ```yaml
  mappers:
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

Now let's re-run our pipeline but this time with the mapper. You run it by calling:

> `meltano run tap-csv hide-ips target-duckdb`

To view the data again, run the helper again: 

> `./meltano_tut select_db`

## Step 8 - Celebrate your success 🎉

That was fun and quick! Now try to run 

> `meltano dragon` 

just for the fun of it! 🐉

## Next Steps

More things you can explore inside this codespace: 

  * **Meltano VS Code Extension**

    Do you see this little dragon on the left hand side? 
    
    ![Dragon](/meltano-ext.png)

    That's the [Meltano VS Code extension](https://marketplace.visualstudio.com/items?itemName=z3z1ma.meltano-power-user). It allows you to view and add all possible taps & targets we currently have on Meltano Hub. Take a look at them!

  * **Add another target**

    Why don't you try to add a second output? Try to add `target-jsonl` and do a `meltano run tap-csv target-jsonl`.

  * **Add another tap**

    Next, try to add another tap, for instance the `tap-carbon-intensity`, play around with it and push the data into either target.

Once you're done, head over to the docs and check out our great [**getting started tutorial**](https://docs.meltano.com/) for more details, add a [**job**](https://docs.meltano.com/reference/command-line-interface#job) **and** [**schedule**](https://docs.meltano.com/reference/command-line-interface#schedule) to easily orchestrate your extract & load processes, and [**deploy it to production**](https://docs.meltano.com/guide/production).

# (Coming Soon 🏗️) Advanced Tutorial #

- Explore different [replication methods](https://docs.meltano.com/guide/integration#replication-methods) to run [incremental](https://docs.meltano.com/guide/integration#incremental-replication-state) loads instead of [full syncs](https://docs.meltano.com/guide/integration#full-table-replication)
- Explore deploying to Github Actions.
- Explore using [environments](https://docs.meltano.com/concepts/environments) to change configuration at runtime
- Explore [running dbt](https://docs.meltano.com/guide/transformation) and other tools with Meltano
