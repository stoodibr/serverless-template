import elasticapm
import json

elasticapm.instrument()
apm = elasticapm.Client()


def response(func, event, context, transaction_name=''):
    """
    Calls `func(event, context)` and returns a properly formatted response,
    also reporting the transaction results to APM using either the given
    `transaction_name` or `func`'s name.
    """
    if not transaction_name:
        transaction_name = func.__name__

    apm.begin_transaction('Request')
    elasticapm.set_custom_context({
        'event': event,
        'function_name': context.function_name,
        'aws_request_id': context.aws_request_id,
    })
    # https://docs.aws.amazon.com/pt_br/lambda/latest/dg/python-context-object.html

    try:
        body = func(event, context)
        response = {'statusCode': 200, 'body': json.dumps(body)}
        return response
    except Exception as e:
        error = {'code': type(e).__name__, 'message': str(e)}
        body = {'errors': [error]}
        response = {'statusCode': 500, 'body': json.dumps(body)}
        apm.capture_exception()
        return response
    finally:
        apm.end_transaction(transaction_name)
