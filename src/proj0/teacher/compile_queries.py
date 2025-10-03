# Run this script with `python3 compile_queries.py` to compile staff .sql query files into student .sql query files.
# YOU SHOULD ALWAYS MANUALLY CHECK THE COMPILED FILES AFTERWARD FOR CORRECTNESS!
# The script assumes the staff query file is well formed, e.g. it doesn't do special
# error handling if you forgot to add `-- END SOLUTION`.

"""
1) Stripping solutions with a prompt:
--- BEGIN SOLUTION
SELECT *
FROM table
WHERE condition;
-- END SOLUTION

will produce:

SELECT 'YOUR CODE HERE';

2) Stripping solutions without a prompt:
--- BEGIN SOLUTION NO PROMPT
SELECT *
FROM table
WHERE condition;
-- END SOLUTION

will produce:

<empty file>

3) Uncommenting starter code:

-- BEGIN STARTER
-- SELECT ____
-- FROM _____
-- WHERE _____;
-- END STARTER

will produce:

SELECT ____
FROM _____
WHERE _____;
"""

import os

QUERIES_DIR = 'queries'
COMPILED_DIR = 'compiled'


def main():
    files = []
    for (dir_path, dir_names, file_names) in os.walk(QUERIES_DIR):
        if dir_path != f'{QUERIES_DIR}/.ipynb_checkpoints':
            for name in file_names:
                if name.endswith('.sql'):
                    files.append(name)

    files.sort()

    output_text = []
    for file_name in files:
        with open(f'{QUERIES_DIR}/{file_name}', 'r') as f:
            output = remove_solutions(f.read())
            output = uncomment_starter_code(output)
            output_text.append(output)

    compile_query_files(files, output_text)
    files_list = "\n".join(files)
    print(f'Compiled {len(files)} files:\n{files_list}')


def compile_query_files(file_names, output_text):
    if not os.path.exists(COMPILED_DIR):
        os.makedirs(COMPILED_DIR)

    for fname, text in zip(file_names, output_text):
        with open(f'{COMPILED_DIR}/{fname}', 'w') as f:
            f.write(text)


def remove_solutions(text):
    text = text.split('\n')
    output_lines = []
    begin_solution = False

    for line in text:
        if line.strip() == '-- BEGIN SOLUTION':
            begin_solution = True
            output_lines.append("SELECT 'YOUR CODE HERE';")
        elif line.strip() == '-- BEGIN SOLUTION NO PROMPT':
            begin_solution = True
        elif line.strip() == '-- END SOLUTION':
            begin_solution = False
        elif begin_solution:
            continue
        else:
            output_lines.append(line)

    output = '\n'.join(output_lines)
    return output


def uncomment_starter_code(text):
    text = text.split('\n')
    output_lines = []
    begin_starter = False

    for line in text:
        if line.strip() == '-- BEGIN STARTER':
            begin_starter = True
        elif line.strip() == '-- END STARTER':
            begin_starter = False
        elif begin_starter:
            line = line.strip()
            line = line[3:] # remove '-- ' prefix
            output_lines.append(line)
        else:
            output_lines.append(line)

    output = '\n'.join(output_lines)
    return output


if __name__ == '__main__':
    main()
