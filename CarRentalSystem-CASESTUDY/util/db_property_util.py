def get_property_string(file_path):
    props = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                props[key] = value
    return props

