rivers = {
    'nile': 'egypt',
    'Kaveri': 'India',
    'padma': 'bangladesh'
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()  
print("Rivers in the dictionary:")
for river in rivers.keys():
    print(river.title())

print()  
print("Countries in the dictionary:")
for country in rivers.values():
    print(country.title())