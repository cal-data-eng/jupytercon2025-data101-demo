#!/bin/bash

DB_USER=$(whoami)
DATABASE_NAME=billboard
SCHEMA_FILE=billboard.sql
HOT_ONE_HUNDRED_TABLE=hot_100
TIKTOK_TOP_FIFTY_TABLE=tiktok_top_50

### Use these commands to create a dump of the database into SCHEMA_FILE
# NOTE: If you want to use a specific DB host, use the command below instead
# CONNECTION="-h $DB_HOST -U $DB_USER -d $DATABASE_NAME --no-owner --no-privileges";
CONNECTION="-U $DB_USER -d $DATABASE_NAME --no-owner --no-privileges";
echo "Dumping schema to $SCHEMA_FILE";
pg_dump --schema-only $CONNECTION \
| grep -v '\\restrict' \
| grep -v '\\unrestrict' \
| grep -v '^-- Dumped by ' \
| grep -v 'set_config' \
| grep -v "^SET" > $SCHEMA_FILE;
pg_dump --data-only --table=$HOT_ONE_HUNDRED_TABLE --table=$TIKTOK_TOP_FIFTY_TABLE $CONNECTION \
| grep -v '\\restrict' \
| grep -v '\\unrestrict' \
| grep -v "^--" \
| grep -v 'set_config' \
| grep -v "^SET" >> $SCHEMA_FILE;

### Use these commands to restore the database from the SCHEMA_FILE after it has been dumped
# This displays an error if the db exists, but is a no-op.
# createdb $DATABASE_NAME;

# Run the statements in SCHEMA_FILE
# psql -d $DATABASE_NAME -a -f $SCHEMA_FILE;
