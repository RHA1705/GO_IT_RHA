import base64

# def get_credentials_users(path):
#     with open(path, 'rb') as f:
#         lines = [line.strip() for line in f.readlines()]
#         row = []
#         for i in lines:
#             i = i.decode()
#             row.append(i)
#         return row

dane = ['andry:uyro18890D', 'steve:oppjM13LL9e']

def encode_data_to_base64(data):
    result = []
    for i in dane:
        i_bytes = i.encode()
        base64_bytes = base64.b64encode(i_bytes)
        base64_i = base64_bytes.decode()
        result.append(base64_i)
    return result

print(encode_data_to_base64(dane))
