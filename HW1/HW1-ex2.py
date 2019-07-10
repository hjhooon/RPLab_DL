input_expression_1 = ["abc{def[ghi]{(jkl}}"]
input_expression_2 = ["abc[def{ghi}{jkl})]"]

def check_parentheses(input_expression):
    L=list(input_expression)
    a_1 = L.count("{")
    a_2 = L.count("}")
    b_1 = L.count("[")
    b_2 = L.count("]")
    c_1 = L.count("(")
    c_2 = L.count(")")
    if (a_1 == a_2 and b_1 == b_2 and c_1 == c_2):
        return print("Balanced")
    else:
        return print("Unbalanced")

check_parentheses(input_expression_1)