from cgi import parse_qs

def app(environ, start_response):
        data = ""
        d = parse_qs(environ['QUERY_STRING'])
        for q in d:
            data += q + '='
            for s in d[q]:
                    data += s
            data += '\n'
            
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return [data]
        
