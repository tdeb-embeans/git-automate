import os
import git
import sqlite3
import glob
import shutil
from datetime import date, datetime

path='/home/incise/codes/autotest/automation-test'

def git_clone(repo):
	git.Git().clone(repo)

def git_pull():
	git.Git().pull()

#def git_tags()
#	git.Git().tag()

def getAllFilesRecursive(root):
	files = [file for file in glob.glob(root + '/*/**/*.txt', recursive=True)]    
	return files

def parse_data(file_path):
	f = open(file_path, "r")
	words = f.read().split()
	return words

def main():
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()

	# Delete the old folder
	if os.path.exists(path) : 
		if len(os.listdir(path)) > 0:
			shutil.rmtree(path)
	#os.removedirs(path)
	# Clone the repo
	git_clone('https://github.com/Incise-info/automation-test.git')
	# get the all list of files
	files = getAllFilesRecursive(path)
	# from the list read one by one
	i = 0
	for f in files:
		id = i + 1
		words = parse_data(f)
		# extract the data from file
		# seperate the components
		date_n = words[0]
		time = words[2]
		test_case_id = words[1]
		branch = "master"
		result = words[3]
		tag = "RELEASE1.0"		
		params = ( test_case_id, '2006-01-05', result, tag, branch)
		
		print ( 'date', date )
		print ( 'time', time)
		print ( 'test_case_id', test_case_id)
		print ( 'result', result) 
		# put the data to the sqlite db
		c.execute('INSERT INTO testprj_testcase VALUES (NULL,  ?, ?, ?, ?, ?)', params)
		# Save (commit) the changes
		conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

	


if __name__ == '__main__':
    main()

