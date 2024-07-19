students = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    with open(output, 'w') as output_file:
        # Iterating over the keys of the first applicant to write the header
        # header = ",".join(source[0].keys()) + "\n"
        # output_file.write(header)

        # Iterating over each applicant and writing their data to the file
        for applicant in source:
            line = ",".join(str(applicant[key]) for key in applicant.keys()) + "\n"
            output_file.write(line)

print(save_applicant_data(students, 'output.txt'))
