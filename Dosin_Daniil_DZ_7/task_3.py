import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
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
