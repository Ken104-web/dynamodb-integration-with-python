import boto3

 
dynamodb = boto3.resource('dynamodb')


table = dynamodb.create_table(
    TableName = 'Users',
    KeySchema = [
         {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
         {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
     ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print('Table status:', table.table_status)

table = dynamodb.Table('Users')



 # insert data
table.put_item(
    Item={
        'username': 'Mwangi',
        'last_name': 'Warui',
        'first_name': 'Ken',
        'age': 21,
        'account_type': 'standard_user',
    }
)

# retrive data

resp = table.get_item(
        Key={
            'username':'Mwangi',
            'last_name':'Warui',
            }
        )

item = resp['Item']
print(item)
