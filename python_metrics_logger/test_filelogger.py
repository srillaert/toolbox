from metricslogger import FileLogger
import os

def test_FileLogger_newfile():
    file_name = "test_file.csv"
    if os.path.exists(file_name):
        os.remove(file_name)

    file_logger = FileLogger(file_name, "myheader")

    assert os.path.exists(file_name)
    with open(file_name, "r") as log_file:
        content = log_file.read()
    assert content == "myheader\n"

    file_logger.log("myline")

    with open(file_name, "r") as log_file:
        content = log_file.read()
    assert content == "myheader\nmyline\n"
    assert os.path.exists(file_name)
    os.remove(file_name)