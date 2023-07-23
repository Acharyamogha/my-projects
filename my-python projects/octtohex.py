def octal_to_decimal(octal):
 decimal = 0
 power = 0
 while octal > 0:
  last_digit = octal % 10
  decimal += last_digit * (8 ** power)
  octal //= 10
  power += 1
 return decimal
def decimal_to_hexadecimal(decimal):
 hexadecimal = ""
 while decimal > 0:
  remainder = decimal % 16
  if remainder < 10:
   hexadecimal = str(remainder) + hexadecimal
  else:
   hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
  decimal //= 16
 return hexadecimal

# Example usage
try:
 octal = int(input("Enter an octal number: "))
 decimal = octal_to_decimal(octal)
 hexadecimal = decimal_to_hexadecimal(decimal)
 print("Hexadecimal equivalent:", hexadecimal)
except ValueError:
 print("Invalid input: Not a valid octal number")