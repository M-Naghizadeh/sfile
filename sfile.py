
def sfile(path, args = None, file_type = 'file', script= None):
    '''
    A simple file management application for python users
    '''
    # import necesarry libraries
    import os
    import re

    # search for files using regular expression in python
    files_list = []
    def get_file(path):
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                files_list.append(path + file)
            elif os.path.isdir(path+file):
                files_list.append(path+file)
                get_file(path + file + '/')
    get_file(path)
    search_results = []
    for file in files_list:
        res = []
        for arg in args:
            pattern = re.compile(arg)
            if bool(re.search(pattern, file)):
                res.append('true')
            else:
                res.append('false')
        if 'false' in res:
            continue
        else:
            search_results.append(file)

    end_results = []
    if file_type == 'file':
        for file in search_results:
            if os.path.isfile(file):
                end_results.append(file)
    if file_type == 'dir':
        for file in search_results:
            if os.path.isdir(file):
                end_results.append(file)

    # execution of an application
    if script == None: 
        return end_results
    else:
        for file in end_results:
            text = script
            text = text.replace('{}', "'"+file+"'")
            exec(text)
