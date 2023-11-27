def get_cats_info(path, search_id):
    with open(path, 'r') as fh:
        lines = [line.strip() for line in fh.readlines()]

    rows = [{'id': line[0], 'name': line[1], 'ingredients': line[2:]} for line in (entry.split(',') for entry in lines)]
    for i in rows:
        for val in i.values():
            if val == search_id:
                return i
    

print(get_cats_info('text.txt', '60b90c1c13067a15887e1ae1'))