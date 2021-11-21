import os

MY_VALUES = ['settings', 'mainapp', 'adminapp', 'authapp']
MY_KEYS = 'my_project'
MY_DISC = {MY_KEYS: MY_VALUES}
dir_path = [os.makedirs(os.path.join(MY_KEYS, i)) for i in MY_VALUES if not os.path.exists(os.path.join(MY_KEYS, i))]
my_path = os.path.join(os.path.abspath(os.getcwd()), MY_KEYS)
for i in MY_VALUES:
    print(os.path.join(my_path, i))
