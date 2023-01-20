
### Full table all in ###
Starting with the most basic and simple replication method



run meltano run el_without_ips again

.... Beginning full_table sync of 'raw_customers'...

.... message=Loading 29 rows into 'raw."raw_customers"'
run ./meltano_tut select_db

... no change, same data right? because we're doing a "full table" sync.


Next step: delete one line, and run again.

delete "1,Ethe,Book,ebook0@twitter.com,67.61.243.220"

... Loading 28 rows into 'raw."raw_customers"'
...  BUt Ethe is still there..

Add a line: 
"30,Ethe_is_back,Book,ebook0@twitter.com,67.61.243.220"

meltano run el_without_ips
./meltano_tut select_db

(now has 30 entries!)



Next up, let's add metadata!
add_metadata_columns = True....

  loaders:
  - name: target-duckdb
    variant: jwills
    pip_url: target-duckdb~=0.4
    config:
      filepath: output/my.duckdb
      default_target_schema: raw
      add_metadata_columns: True

2023-01-19T09:10:01.896666Z [info     ] time=2023-01-19 09:10:01 name=target_duckdb level=INFO message=Table '"raw_customers"' exists cmd_type=elb consumer=True name=target-duckdb producer=False stdio=stderr string_id=target-duckdb
2023-01-19T09:10:01.902129Z [info     ] time=2023-01-19 09:10:01 name=target_duckdb level=INFO message=Adding column: ALTER TABLE raw."raw_customers" ADD COLUMN "_sdc_batched_at" timestamp cmd_type=elb consumer=True name=target-duckdb producer=False stdio=stderr string_id=target-duckdb
2023-01-19T09:10:01.923412Z [info     ] time=2023-01-19 09:10:01 name=target_duckdb level=INFO message=Adding column: ALTER TABLE raw."raw_customers" ADD COLUMN "_sdc_deleted_at" varchar cmd_type=elb consumer=True name=target-duckdb producer=False stdio=stderr string_id=target-duckdb
2023-01-19T09:10:01.946326Z [info     ] time=2023-01-19 09:10:01 name=target_duckdb level=INFO message=Adding column: ALTER TABLE raw."raw_customers" ADD COLUMN "_sdc_extracted_at" timestamp cmd_type=elb consumer=True name=target-duckdb producer=False stdio=stderr string_id=target-duckdb
Change and remove a column!

delete: 29,Edie,Corderoy,ecorderoys@nationalgeographic.com,1

  - name: target-duckdb
    variant: jwills
    pip_url: target-duckdb~=0.4
    config:
      filepath: output/my.duckdb
      default_target_schema: raw
      add_metadata_columns: True
      hard_delete: True
    






## Deploying Meltano into Github Actions.

Finally, we will deploy our little demo into Github Actions. 

*Warning*: This will eat up your GitHub Actions minutes, you should have free ones, but just take care.

```yaml
name: Pipeline for testing codespaces demo

on: 
  workflow_dispatch:
  schedule:
    - cron:  '30 08 * * *'

jobs:
  install_plugins:
    name: "meltano_install"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3.2.0

      - name: Run your Meltano on schedule
        uses: devcontainers/ci@v0.2
        with:
          push: never
          runCmd: meltano install

run_el:
    name: "meltano_run_el"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3.2.0

      - name: Run your Meltano on schedule
        uses: devcontainers/ci@v0.2
        with:
          push: never
          runCmd: meltano run el_without_ips
```yaml

This runs now at 8:30 every morning, 
OR if you click on it. Try it out!

(insert image!)


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
