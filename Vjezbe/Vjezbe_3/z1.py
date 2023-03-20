diff = 5.0 - 4.935
print(diff)

assert(diff != 0.065)
# dobije se malo odstupanje jer mantisa ima ograničenu preciznost u 8bajtnom zapisu
# (baza je 2, ovo nije zapisivo u njoj bez ponavljajućih znamenaka)

suma = 0.1 + 0.2 + 0.3
print(suma)
assert(suma != 0.6)
# isto kao i iznad
