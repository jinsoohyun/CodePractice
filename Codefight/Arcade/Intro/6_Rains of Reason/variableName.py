from ast import parse

def is_valid_variable_name(name):
    try:
        parse('{} = None'.format(name))
        return True
    except:
        return False

def variableName(name):
    return is_valid_variable_name(name)
