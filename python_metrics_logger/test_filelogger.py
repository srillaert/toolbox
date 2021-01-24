from metricslogger import FileLogger
import os
import pytest

test_file_name = "test_file.csv"

def get_file_content():
	with open(test_file_name, "r") as log_file:
		content = log_file.read()
		return content

@pytest.fixture()
def test_file():
	if os.path.exists(test_file_name):
		os.remove(test_file_name)
	yield test_file_name
	os.remove(test_file_name)

def test_FileLogger_existingfile(test_file):
	with open(test_file_name, "w") as log_file:
		log_file.write("previouscontent\n")
	
	file_logger = FileLogger(test_file_name, "myheader")
	# header is not being added when the file already existed
	assert get_file_content() == "previouscontent\n"

	file_logger.log("myline")
	assert get_file_content() == "previouscontent\nmyline\n"

def test_FileLogger_newfile(test_file):
	file_logger = FileLogger(test_file_name, "myheader")	
	assert get_file_content() == "myheader\n"

	file_logger.log("myline")
	assert get_file_content() == "myheader\nmyline\n"
