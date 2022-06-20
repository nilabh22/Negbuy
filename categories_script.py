def run():
    with open('/Users/amir/Code/Negbuy/static/categories/categories.txt') as file:
        for line in file:
            category = line.strip().split('>')[0]
            category_file_path = '/Users/amir/Code/Negbuy/static/categories/'+str(category).strip()+'.txt'
            category_file = open(category_file_path, "a")
            category_file.write(line)
            category_file.close()

run()