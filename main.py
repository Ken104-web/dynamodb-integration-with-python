import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName = 'Users',
    keySchema = [
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

table.put_item(
    Item={
        'username': 'johndoe',
        'last_name': 'Doe',
        'first_name': 'John',
        'age': 25,
        'account_type': 'standard_user',
    }
)