import duckdb

# to use a database file (not shared between processes)
con = duckdb.connect(database='output/my.duckdb', read_only=True)

con.execute("SELECT * FROM raw.raw_customers")
print(con.fetchall())