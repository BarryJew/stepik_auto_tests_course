# Пример в уроке
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

# Решение задания

def test_input_text(full_string, substring):
    assert (substring in full_string), f"expected '{substring}' to be substring of '{full_string}'"