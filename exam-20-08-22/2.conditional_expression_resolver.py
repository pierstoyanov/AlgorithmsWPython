line = input()


def resolve_expression(expression):
    if '?' not in expression:
        return int(expression)

    expression = expression.replace(' ', '')
    bool_val, choices = expression.rsplit('?', 1)
    true, false = choices.rsplit(':', 1)

    if bool_val == 't':
        return resolve_expression(true)
    if bool_val == 'f':
        return resolve_expression(false)


print(resolve_expression(line))
