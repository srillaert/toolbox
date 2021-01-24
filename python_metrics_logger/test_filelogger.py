from metricslogger import FileLogger
import os

def get_nonexisting_test_file_name():
    file_name = "test_file.csv"
    if os.path.exists(file_name):
        os.remove(file_name)
    return file_name

def test_FileLogger_existingfile():
    file_name = get_nonexisting_test_file_name()

    with open(file_name, "w") as log_file:
        log_file.write("previouscontent\n")
    
    file_logger = FileLogger(file_name, "myheader")

    with open(file_name, "r") as log_file:
        content = log_file.read()
    assert content == "previouscontent\n" # header is not being added when the file already existed

    file_logger.log("myline")

    with open(file_name, "r") as log_file:
        content = log_file.read()
    assert content == "previouscontent\nmyline\n"

    os.remove(file_name)

def test_FileLogger_newfile():
    file_name = get_nonexisting_test_file_name()
    file_logger = FileLogger(file_name, "myheader")    

    with open(file_name, "r") as log_file:
        content = log_file.read()
    assert content == "myheader\n"

    file_logger.log("myline")

    with open(file_name, "r") as log_file:
        content = log_file.read()
    assert content == "myheader\nmyline\n"
    os.remove(file_name)
