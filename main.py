# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4]) # or just [:4]
print(credit_number[5:9])
print(credit_number[5:19]) # or just [5:]
print(credit_number[-1]) # negative index, starts from the end of the string
print(credit_number[-2])
print(credit_number[::2])
print(credit_number[::3])