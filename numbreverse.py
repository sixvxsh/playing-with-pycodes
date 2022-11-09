num = int(input())
yekan = num % 10
sadgan = num // 100
komak_dahgan = num // 10
dahgan = komak_dahgan % 10
new_num = str(yekan) + str(dahgan) + str(sadgan)

print(2*int(new_num))
