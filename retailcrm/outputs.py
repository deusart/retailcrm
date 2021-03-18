def output_empty(*str):
    pass

def output_all(*str):
    print(str[0], str[1])

def output_debug(*str):
    if str[0] in ('[Debug]','[Error]'):
        print(str[0], str[1])

def output_main(*str):
    if str[0] in ('[Main]','[Error]'):
        print(str[0], str[1])