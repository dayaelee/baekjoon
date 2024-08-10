def work():
    st1 = None
    result = []
    while st1 != ".":
        st1 = input("")

        s_list = []
        replace_list = []

        for idx, ch in enumerate(st1):
            if (ord(ch)) == 40 or (ord(ch)) == 41 or (ord(ch)) == 91 or (ord(ch)) == 93 or (ord(ch)) == 123 or\
                    (ord(ch)) == 125:
                s_list.append(ch)
            if ch == ")" or ch == "}" or ch == "]":
                replace_list.append(ch)

        list_str = ''.join(s_list)

        for erode in replace_list:
            if erode == ")":
                list_str = list_str.replace("()", "")
            elif erode == "}":
                list_str = list_str.replace("{}", "")
            elif erode == "]":
                list_str = list_str.replace("[]", "")

        if list_str == '':
            result.append('yes')
        else:
            result.append('no')
    result.pop()
    print('\n'.join(result))


work()
