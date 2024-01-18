def getResponses(valid_auth_tokens, requests):
    def validate_request_type(request_type):
        return request_type.upper() in ["GET", "POST"]

    def validate_token(token, valid_auth_tokens):
        return token in valid_auth_tokens

    def validate_csrf(csrf_token):
        # Modify this function based on your CSRF validation requirements
        # Example: Check if CSRF token contains non-alphanumeric characters and has a length less than 8
        return not any(c.isalnum() for c in csrf_token) and len(csrf_token) < 8

    def parse_url_parameters(parameters):
        parsed_parameters = {}
        for param in parameters.split("&"):
            key, value = param.split("=")
            parsed_parameters[key] = value
        return parsed_parameters

    def process_request(valid_auth_tokens, request):
        request_type, url = request
        url_parts = url.split("?")
        url_parameters = url_parts[1] if len(url_parts) > 1 else ""
        params = parse_url_parameters(url_parameters)

        token = params.get('token', '')
        csrf_token = params.get('csrf', '') if request_type == 'POST' else None

        if (
            validate_request_type(request_type)
            and validate_token(token, valid_auth_tokens)
        ):
            if request_type == 'POST' and validate_csrf(csrf_token):
                response = f"VALID,{','.join(f'{key},{value}' for key, value in params.items())}"
            elif request_type == 'GET':
                response = f"VALID,{','.join(f'{key},{value}' for key, value in params.items() if key != 'token')}"
            else:
                response = "INVALID"
        else:
            response = "INVALID"

        return response

    responses = []

    for request in requests:
        response = process_request(valid_auth_tokens, request)
        responses.append(response)

    return responses

# Sample Input
valid_auth_tokens = ["et51u8i9p1q7", "b8nn5j4om76v", "r5b019lmlp09"]
requests = [
    ["GET", "https://example.com/?token=et51u8i9p1q7&id=2e3rt&name=alex"],
    ["POST", "https://example.com/?token=r5b019lmlp09&csrf=ia+09&id=u78we&name=evan"]
]

# Get Responses
output = getResponses(valid_auth_tokens, requests)

# Sample Output
for result in output:
    print(result)
