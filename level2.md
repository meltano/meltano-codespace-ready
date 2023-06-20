In level 2 of the demo you will:
- remove the plain text IP adresses from the database
- create a named job to make calling your new pipeline easier

# Step 1 - Add the transform-field mapper

Notice that the data you just viewed had plain IP adresses inside of it? Let's quickly get rid of those!

Add a "mapper" to do slight modifications on the data we're sourcing here.

> `meltano add mapper transform-field`

# Step 2 - Configure the mapper to remove plain text IP adresses

 Now paste the following config below the `pip_url` for the `transform-field` mapper in your `meltano.yml` file.

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

# Step 3 - Add a job name to your pipeline

You already know how `meltano run` kind of works. So let's wrap the steps of the pipeline behind the run command into a "job" so we can call it with just one word.

Run:
> `meltano job add el_without_ips --tasks "[tap-csv hide-ips target-duckdb]"`

This will add the following line into your meltano.yml file:

 ```yaml
jobs:
- name: el_without_ips
  tasks:
  - tap-csv hide-ips target-duckdb
 ```

Now let's re-run our pipeline

# Step 4 - Run the pipeline calling the job
Now simply run the "job":

> `meltano run el_without_ips`

# Step 5 - Check that it worked

To view the data again, run the helper again: 

> `./meltano_tut select_db`

# Step 6 - Celebrate your success 🎉

That was fun and quick! Now try to run 

> `meltano dragon` 

just for the fun of it! 🐉

# Next steps - level 3 for more
Next we want to explore the rest of the demo and go further, open up ["the level 3 instructions"](level3.md) for that!
