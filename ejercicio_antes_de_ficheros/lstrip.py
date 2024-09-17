# str.lstrip([chars])¶
# Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
nuevo_texto = texto.lstrip(',:%_#')
print(nuevo_texto)