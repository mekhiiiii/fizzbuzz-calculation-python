count = 1

fizzbuzz_calculation = 0

fizz_calculation = 0

buzz_calculation = 0

while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        fizzbuzz_calculation = fizzbuzz_calculation + count
    elif count % 3 == 0:
        fizz_calculation = fizz_calculation + count
    elif count % 5 == 0:
        buzz_calculation = buzz_calculation + count      
    count += 1

print("The sum of all FIZZ numbers is: " + str(fizz_calculation))
print("The sum of all BUZZ numbers is: " +str(buzz_calculation))
print("The sum of all FIZZBUZZ numbers is: " + str(fizzbuzz_calculation))