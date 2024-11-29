def make_parse_get():
    def parse_get(string):
        req_type, path, net_type = string.split()
        return dict([('Request Method',req_type), ('Request URL', path), ('net_type', net_type)])
    return parse_get