# Use this code snippet in your app.
import boto3
from botocore.exceptions import ClientError


def get_secret():
    # testLUISKey, RDSUserPwd
    secret_name = "testLUISKey"
    endpoint_url = "https://secretsmanager.us-east-2.amazonaws.com"
    region_name = "us-east-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        endpoint_url=endpoint_url
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
    else:
        # Decrypted secret using the associated KMS CMK
        # Depending on whether the secret was a string or binary, one of these fields will be populated
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']
    return get_secret_value_response['SecretString']

# 返回密码，参数等等
#{"username":"raidenyu","password":"raiden's password","engine":"mysql","host":"maindb.cdh6uj0q1vxk.us-east-2.rds.amazonaws.com","port":3306,"dbname":"raidendb","dbInstanceIdentifier":"maindb"}
print(get_secret())