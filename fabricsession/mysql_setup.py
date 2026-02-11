import datetime
from fabric import Connection

# Read password from file
with open("password.txt") as f:
    password = f.read().strip()

# SSH Connection
connection = Connection(
    host="127.0.0.1",
    user="waka",
    connect_kwargs={"password": password}
)

# Timestamp (optional)
time_mod = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


# ---------------------------------------------------
# 1. Install MySQL Server
# ---------------------------------------------------
def install_mysql():
    print("Installing MySQL Server...")

    connection.run("sudo apt update -y")
    connection.run("sudo apt install mysql-server -y")

    print("MySQL Installed Successfully ✅")


# ---------------------------------------------------
# 2. Create a Database
# ---------------------------------------------------
def create_database():
    db_name = "fabric_db"

    print(f"Creating database: {db_name}")

    connection.run(
        f"sudo mysql -e \"CREATE DATABASE IF NOT EXISTS {db_name};\""
    )

    print("Database Created Successfully ✅")


# ---------------------------------------------------
# 3. Import SQL Dump File
# ---------------------------------------------------
def import_sql_dump():
    db_name = "fabric_db"

    # Path to your SQL dump file
    dump_file = "/home/waka/ALU/Sessions/FabricSession/dumps/mydump.sql"

    print("Importing SQL dump...")

    connection.run(
        f"sudo mysql {db_name} < {dump_file}"
    )

    print("SQL Dump Imported Successfully ✅")


# ---------------------------------------------------
# Main Execution
# ---------------------------------------------------
def setup_mysql():
    install_mysql()
    create_database()
    import_sql_dump()


# Run everything
setup_mysql()
