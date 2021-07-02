try:
    with open('test1.log', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "asd.log" in line:
                with open('new.log', 'a') as new_file:
                    new_file.write(line)
except Exception as e:
    print(e)