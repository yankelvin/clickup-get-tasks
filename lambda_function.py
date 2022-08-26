import os
import json
from bson import json_util

from services.MongoDB import MongoDB

connectionString = os.environ.get('CONNECTION_STRING', None)
mongodb = MongoDB(connectionString=connectionString)


def lambda_handler(event, context):
    try:
        tasks = mongodb.get_all_tasks()
        documents = json.loads(json_util.dumps(list(tasks)))
        
        for task in documents:
            task.pop("_id", None)

        return {
            "statusCode": 200,
            "headers": {},
            "body": json.dumps(documents)
        }
    except Exception as ex:
        print(ex)
        return ex
