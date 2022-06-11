#!/bin/bash

psql -v ON_ERROR_STOP=1 --username $DB_USER_NAME --dbname $DB_NAME -f projeto_sql
