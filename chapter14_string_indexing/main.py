# begin : end : step
credit_card_number = "1234-5678-9012-3456"
print(credit_card_number[0])
print(credit_card_number[:4])
print(credit_card_number[5:9])
print(credit_card_number[5:])
print(credit_card_number[-5]) # counts from right to left with negative index
print(credit_card_number[::2]) # every two chars
print(f"XXXX-XXXX-XXXX-{credit_card_number[-4:]}") # show only last 4 chars