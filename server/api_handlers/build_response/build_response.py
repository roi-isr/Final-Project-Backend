def build_response(data, status_code):
    response = data
    if not status_code:
        return response
    response.status_code = status_code
    return response
