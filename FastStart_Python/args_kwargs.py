
# могу вводить кучу параметров - они преобразуются в tuple
# могу вводить кучу параметров для анализа в качестве словаря kwargs
def foo(*args, **kwargs):

    action = kwargs.get('action', 'sum')
    return_type = kwargs.get('return_type', 'int')

    if action == 'sum':
        answer = (sum(args))

    elif action == 'avg':
        answer = (sum(args)/len(args))

    if return_type == 'int':
        print(int(answer))

    elif return_type == 'float':
        print(float(answer))



if __name__ == '__main__':
    foo(1,2,3, action='sum', return_type = 'float')
    foo(1,2,3, action='avg', return_type = 'int')
