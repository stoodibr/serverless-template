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
