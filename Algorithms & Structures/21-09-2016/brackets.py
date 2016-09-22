# s is a string containing symbols '(', ')', '[', ']'
# functions returns True, if s is correct brackets sequence, False otherwise
# use stack!
def check_brackets(s):
    stack = []
    pairs = {')': '(', ']': '['}
    for i in range(len(s)):
        if s[i] in pairs.keys():
            if len(stack) != 0 and stack[-1] == pairs[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False


def test_check_brackets(s, answer):
    # print(check_brackets(s))
    assert check_brackets(s) == answer

test_check_brackets('()()', True)
test_check_brackets('[[]]', True)
test_check_brackets('([])[()]', True)
test_check_brackets('(]', False)
test_check_brackets('[)', False)
test_check_brackets('([)]', False)
test_check_brackets(')', False)
test_check_brackets('()]', False)
test_check_brackets('(([]())', False)