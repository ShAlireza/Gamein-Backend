set -e

su - postgres bash -c "
    createuser -E -w $DB_USER << '$DB_PASS';
    createdb $DB_NAME -O $DB_USER;
    "