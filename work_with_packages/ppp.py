try:
    with open("work_with_files_1.txt", "r+", encoding="utf-8") as file:
        content = file.read().strip('\n')
        print(content)[::-1]
         
except FileExistsError:
    print("file hot found")