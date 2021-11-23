# The file recursion program

import os


def find_files_walking(suffix, path, result):
    """Find the target files with specific suffix recursively.
    
    Argus:
        suffix(str): the target file will be selected
        path(str): the target dir will search
        result(list): a array for result
    """
    
    items = os.listdir(path)
    
    for item in items:
        current_path = os.path.join(path, item)
        
        if os.path.isfile(current_path) and current_path.endswith(suffix):
            result.append(current_path)
        
        if os.path.isdir(current_path):
            find_files_walking(suffix, current_path, result)


def find_files(suffix, path):
    result = list()
    if os.path.exists(path):
        find_files_walking(suffix, path, result)
    return result 

def test_function(test_dir, file_type):
    results = find_files(file_type, test_dir)
    print('the file list is: ')
    for file in sorted(results):
        print(file)



print('--- test 1 ---')
print('find .c in ./testdir')
test_function('./testdir', '.c')
""" expected result:
./testdir/subdir1/a.c
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir5/a.c
./testdir/t1.c
"""


print('--- test 2 ---')
print('find .h in ./testdir')
test_function('./testdir', '.h')
""" expected result:
./testdir/subdir1/a.h
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir5/a.h
./testdir/t1.h
"""


print('--- test 3 ---')
print('find .cpp in ./testdir')
test_function('./testdir', '.cpp')
""" expected result:
empty
"""


print('--- test 4 ---')
print('find .cpp in ./not_exist')
test_function('./not_exist', '.cpp')
""" expected result:
empty
"""