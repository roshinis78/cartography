import datetime

LIST_BUCKETS = {
    'Buckets': [
        {
            'Name': 'bucket-1',
            'CreationDate': datetime.datetime(2014, 4, 16, 18, 14, 49),
            'Region': 'eu-west-1',
        }, {
            'Name': 'bucket-2',
            'CreationDate': datetime.datetime(2015, 7, 24, 4, 8, 29),
            'Region': 'me-south-1',
        }, {
            'Name': 'bucket-3',
            'CreationDate': datetime.datetime(2019, 9, 17, 1, 16, 19),
            'Region': None,
        },
    ],
    'Owner': {
        'DisplayName': 'OWNER_NAME',
        'ID': 'OWNER_ID',
    },
}
