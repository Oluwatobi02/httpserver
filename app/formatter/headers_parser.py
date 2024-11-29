def make_parse_header():
    def parse_header(string_arr):
        headers = []
        for line in string_arr:
            key, val = line.split(': ')
            headers.append((key, val))
        return dict(headers)
    return parse_header