# def func(x):
#     print(x)
#
# func('said')
#
# def func(x, text):
#     print(x)
#     if text == '1':
#         print('text is 1')
#     else:
#         print('text is not 1')
# func('x', '1')
#
# def func(x, text='1000'):
#     print(x)
#     if text == '1':
#         print('text is 1')
#     else:
#         print(text)
# func('x', '11')

def func(x=3, text='3'):
    print(x)
    if text == '1':
        print ('text is 1')
    else:
        print(text)
func()