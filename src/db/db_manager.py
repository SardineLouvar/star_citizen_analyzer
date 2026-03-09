import os

import sqlite3
from src.paths import DB_PATH
from src.io.json_utils import get_json
from src.config_loader import load_config

config = load_config()

con = sqlite3.connect(os.path.join(DB_PATH, "ss_data.db"))
cur = con.cursor()

def make_table(name, headers_arr):
    contents = ", ".join(map(str, headers_arr))
    cur.execute(f"CREATE TABLE IF NOT EXISTS {name}({contents})")


def get_sqlite_type(value):
    if isinstance(value, bool):
        return "INTEGER"
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    else:
        return "TEXT"


def table_exists(name):
    res = cur.execute(f"SELECT name FROM sqlite_master WHERE name = '{name}'")
    return bool(res.fetchone())


def json_into_db(name):
    data = get_json(name)
    if not data:
        print(f"cannot upload {name} as table as does not exist")
        return
    elif data["status"] != "ok":
        print(f"Could not get data from API for {name}")
        return
    elif not data["data"]:
        print(f"no data found for {name}")
        return

    if table_exists(name):
        if config["quiet"] == False:
            print(f"table {name} already exists, no changes made")
        return
    
    columns = []
    column_names = []

    for key, value in data["data"][0].items():
        column_names.append(key)
        columns.append(f"{key} {get_sqlite_type(value)}")
    
    make_table(name, columns)

    # Prepare insert statement
    col_names = ", ".join(column_names)
    placeholders = ", ".join("?" for _ in column_names)
    sql = f"INSERT INTO {name} ({col_names}) VALUES ({placeholders})"

    # Loop through all rows and insert
    rows = [tuple(item[col] for col in column_names) for item in data["data"]]
    cur.executemany(sql, rows)

    con.commit()
    print(f"Inserted {len(rows)} rows into table {name}")


if __name__ == "__main__":
    res = cur.execute("SELECT DISTINCT commodity_name, id_commodity from commodities_prices_all")
    print(res.fetchall())