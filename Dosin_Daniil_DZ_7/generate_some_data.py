import os
import random
from string import ascii_lowercase, digits
from practice import BASE_DIR

letters = ''.join([ascii_lowercase, digits])
folder = os.path.join(BASE_DIR, 'some_data')
os.makedirs(folder, exist_ok=True)
for _ in range(10 ** 3):
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
    f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
    with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
        f.write(f_content)
