import os
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


#Пока не получилось написать парсер. Сделал вот такую штуку - недопарсер(((

# my_project_dir_path = os.path.join(BASE_DIR, 'my_project')
# if not os.path.exists(my_project_dir_path):
#     os.mkdir(os.path.join(BASE_DIR, 'my_project'))
# for i in (
#         (('settings',), ('__init__.py',), ('dev.py',), ('prod.py',)),
#         (('mainapp',), ("__init__.py",), ('models.py',), ('views.py',),
#          ('templates', ("mainapp", 'base.html', 'index.html'))),
#         (('authapp',), ("__init__.py",), ('models.py',), ('views.py',),
#          ('templates', ("authapp", 'base.html', 'index.html')))):
#
#     sub_folder = os.path.join(my_project_dir_path, i[0][0])
#     if not os.path.exists(sub_folder):
#         os.mkdir(os.path.join(my_project_dir_path, i[0][0]))
#
#     for j in i[1:]:
#         if j[0].find('.') != -1:
#             file = os.path.join(sub_folder, j[0])
#             open(file, mode='a').close()
#         else:
#             folder_path = os.path.join(sub_folder, j[0])
#             if not os.path.exists(folder_path):
#                 os.mkdir(folder_path)
#             for s in j[1:]:
#                 if s[0][0].find('.') != -1:
#                     file = os.path.join(folder_path, s[0])
#                     open(file, mode='a').close()
#                 else:
#                     sub_folder_path = os.path.join(folder_path, s[0])
#                     if not os.path.exists(sub_folder_path):
#                         os.mkdir(sub_folder_path)
#                         for s_s in s[1:]:
#                             if s_s.find('.') != -1:
#                                 file = os.path.join(sub_folder_path, s_s)
#                                 open(file, mode='a').close()
#                             else:
#                                 sub_folder_path = os.path.join(sub_folder_path, s_s)
#                                 if not os.path.exists(sub_folder_path):
#                                     os.mkdir(sub_folder_path)

def collect_folders(path_to_find: str, name_to_find: str):
    """
    collects all folders "name" to the one folder "name" in root path
    :param path_to_find: path in what folder find files and directories
    :param name_to_find:  directory to find
    :return:
    """
    list_sub_path = []
    for root, dirs, name in os.walk(path_to_find):
        if (os.path.basename(root)) == name_to_find:
            list_sub_path.append(root)

    finish_dir_name = os.path.join(path_to_find, name_to_find)
    if not os.path.exists(finish_dir_name):
        os.mkdir(finish_dir_name)

    for sub in list_sub_path:
        try:
            shutil.copytree(sub, finish_dir_name, dirs_exist_ok=True)
        except Exception as err:
            print("".join(err.args[0]))


collect_folders(os.path.join(BASE_DIR, 'my_project'), 'templates')
