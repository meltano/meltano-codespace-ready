


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
