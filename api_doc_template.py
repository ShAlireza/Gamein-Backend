import sys


def create_template(api_counts, app_name):
    with open(f'{app_name}.py', 'w') as file:
        for i in range(1, api_counts + 1):
            string = f'""" API {i}.\n\n'
            string += f'Name: \n\n'
            string += f'URL: \n\n'
            string += f'Method: \n\n'
            string += f'Description: \n\n\n '
            string += f' Request json example: \n"""\n\n'
            string += f'Json_{i} = ' + '{\n\n    # Leave Emtpy if not needed' \
                                       '\n\n}\n\n'
            file.write(string)


create_template(int(sys.argv[1]), sys.argv[2])
