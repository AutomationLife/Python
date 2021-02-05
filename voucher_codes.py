print("""
+----------------------+
|ChaseFX Voucher Codes |
+----------------------+
""")

website = "www.chasefx.com/"

discount_amount = int(input("Discount %: "))
voucher_amount = int(input("Amount: "))

code_start = 0
amount = code_start + voucher_amount

for code in range(code_start, amount):
    print(f"{website}?voucherCode={discount_amount}{code}")
    code_start = amount

print("Code Start: ", code_start)