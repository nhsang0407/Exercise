def extract_url(url):
    global protocol, rest
    if "://" in url:
        protocol, rest = url.split("://")
    if "/" in rest:
        hostname, rest = rest.split("/", 1)
    else:
        hostname, rest = rest, ""
    domain_name = hostname.split(".")[1]
    if "/" in rest:
        directory, rest = rest.split("/")
    else:
        directory, rest =  rest, ""

    if "?" in rest:
        filename, query = rest.split("?")
    else:
        filename, query = rest, " "
    return {
        'protocol': protocol,
        'hostname': hostname,
        'domain_name': domain_name,
        'directory': directory,
        'filename': filename,
        'query': query
    }