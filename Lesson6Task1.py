with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        ip_code = line.split(' ')[:1]
        remote_addr = str(ip_code[0])
        temp = line.split('"')[1:]
        other = temp[0].split(' ')[:2]
        request_type = str(other[0])
        requested_resource = str(other[1])
        result = remote_addr, request_type, requested_resource
        print(result)
