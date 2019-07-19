def create_file(filename):
            file = open(filename, 'w+')
            file.closed() 
    
create_file(filename)


 def reading_file(filename):
            with open(filename) as file:
                    read = file.read()
            file.close

reading_file(filename)


def reading_one_line(filename):
            with open(filename) as file:
                    line = file.readline()
                    print(line)
            file.closed 

reading_one_line(filename)


def printing_all_lines(filename):
             with open(filename) as file:
                    for line in file:
                            print(line, end = '')
            file.close

printing_all_lines(filename)


def write_in_file(filename, text_to_write):
            file = open(filename, 'w+')
            file.write(text_to_write)
            file.close

write_in_file(filename, text_to_write)


def append_in_file(filename, text_to_append):
            file = open(filename, 'a+')
            file.write(text_to_append)
            file.close

append_in_file(filename, text_to_append)


def file_position(filename):
            file = open(filename, 'r')
            print(file.tell())
            file.close() 

file_position(filename)


def cursor_initial_position(filename):
            file = open(filename, 'r')
            print(file.seek(0))
            file.close() 

cursor_initial_position(filename)


def writable_file(filename):
            file = open(filename, 'r')
            print(file.writable())
            file.close() 

writable_file(filename)


def flush_file(filename):
            file = open(filename, 'w')
            file.flush()
            file.close() 

flush_file(filename)







                    


