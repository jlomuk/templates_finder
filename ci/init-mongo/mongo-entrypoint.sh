echo '################ MONGO ENTRYPOINT START ################';

mongo -- "$MONGO_INITDB_DATABASE" <<EOF
db = db.getSiblingDB('$MONGO_INITDB_DATABASE']);

db.createCollection('templates');

db.templates.insertMany([
    {
        name: 'UserForm',
        username: 'text',
        registered_date: 'date',
    },
    {
        name: 'OrderForm',
        address: 'text',
        phone: 'phone',
        date_delivery: 'date'
    },
    {
        name: 'OfficeForm',
        email_office: 'email',
        phone_office: 'phone',
    },
    {
        name: 'ChildrenForm',
        firstname: 'text',
        lastname: 'text',
        birthday: 'date'
    }
]);
EOF

echo '################ MONGO ENTRYPOINT END ################';