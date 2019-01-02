import elasticapm

from utils.response import response


def handler(event, context):
    return response(index, event, context, __name__)


@elasticapm.capture_span()
def index(event, context):
    body = {
        'message': 'Go Serverless!'
    }

    if event:
        body['data'] = event

    return body


if __name__ == "__main__":
    # TODO: how to pass along cli arguments?
    #   sls invoke uses --data and --context
    #   python main uses ... ?
    handler({}, {})
