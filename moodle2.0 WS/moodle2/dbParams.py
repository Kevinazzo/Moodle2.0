import MySQLdb
db = MySQLdb.connect('localhost','root','123456789','moodle2')
cur = db.cursor(MySQLdb.cursors.DictCursor)