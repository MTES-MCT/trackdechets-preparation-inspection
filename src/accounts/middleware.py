from ipware import get_client_ip


def reverse_proxy_middleware(get_response):
    def process_request(request):
        client_ip, _ = get_client_ip(request)
        request.META["REMOTE_ADDR"] = client_ip
        return get_response(request)

    return process_request
