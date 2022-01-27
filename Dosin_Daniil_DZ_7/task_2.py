import os
from task_1 import BASE_DIR


# line_yaml_parser

def starter_from_template(path_file_yaml: str, path_where: str) -> bool:
    with open(path_file_yaml, 'r', encoding='utf-8') as fr:
        line = True
        folders_list = list()
        lines_list = list()
        while line:
            line = fr.readline()
            file_dir = line.strip('| -\n')
            found_all_lvls = False
            line_to_find_lvl = line.strip('\n')
            line_lvl = 1  # there are two spaces before lines as default
            if line == '':
                break
            while not found_all_lvls and line:
                ind = line_to_find_lvl.find("|")
                line_to_find_lvl = line_to_find_lvl[ind + 1:]
                line_lvl += ind

                if ind == -1:
                    found_all_lvls = True

            print(f'for line {line_to_find_lvl} and lvl {line_lvl}')

            lines_list.append((line_to_find_lvl, line_lvl))

    i = 0
    while i < len(lines_list):
        if
            continue
        i += 1

    print(folders_list[0])


starter_from_template(os.path.join(BASE_DIR, 'config.yaml'), BASE_DIR)
