fruits={'apple': 40, 'orange': 80, 'grapes': 60}

new_fruits={k for k,v in fruits.items() if v>40 }

print(new_fruits)
