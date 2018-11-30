import json


def handler(event, context):
    body = {
        'message': 'Go Serverless!',
    }

    if event:
        body['data'] = event

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response


if __name__ == "__main__":
    # TODO: how to pass along cli arguments?
    #   sls invoke uses --data and --context
    #   python main uses ... ?
    handler({}, {})
