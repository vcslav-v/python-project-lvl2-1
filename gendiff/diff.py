import json


def generate_diff(file1, file2):
    file1_dictionary = json.load(open(file1))
    file2_dictionary = json.load(open(file2))

    combined_dictionary = file1_dictionary.copy()
    combined_dictionary.update(file2_dictionary)

    result = '{\n'

    for key, value in combined_dictionary.items():
        value_dictionary1 = file1_dictionary.get(key)
        value_dictionary2 = file2_dictionary.get(key)

        if value_dictionary1 is None:
            result = '{0}  + {1}: {2}\n'.format(result, key, value)
        elif value_dictionary2 is None:
            result = '{0}  - {1}: {2}\n'.format(result, key, value)
        elif value_dictionary1 != value_dictionary2:
            result = '{0}  - {1}: {2}\n'.format(result, key, value_dictionary1)
            result = '{0}  + {1}: {2}\n'.format(result, key, value_dictionary2)
        else:
            result = '{0}    {1}: {2}\n'.format(result, key, value)

    result += '}'

    return result
