# Python-Postgres game matching app

Simple project in Python and Postgres

## How it works

1. It implements tournament between players.
2. It matches players using Swiss pairing.

## Dependencies
- [Python](https://www.python.org/) version 2.7.x or higher
- [PostgresSQL](http://www.postgresql.org/) version 9.4.x  or higher
- [pip](https://pip.pypa.io/en/latest/installing.html) version 1.5.4 or higher
- [bleach](http://bleach.readthedocs.org/en/latest/index.html) 1.4.1 or higher


## Quick Start
### Checking Environment
```bash
python --version
psql --version
```

should show proper versions of Python and Postgres.

### Installing a dependency
```
pip install bleach
```

### Creating a database and tables
```bash
cd /where/your/project/root/is
psql
CREATE DATABASE tournament;
\c tournament
\i tournament.sql
```

Enter ```\q``` to quit ```psql```.

### Running the Test Suite
```bash
python tournament_test.py
```

Yay, no error!