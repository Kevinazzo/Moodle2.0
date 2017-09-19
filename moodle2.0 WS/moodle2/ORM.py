class user:
	def __init__(self, _id, _username, _role):
		self.id = _id
		self.username = _username
		self.role = _role
	def __json__(self):
		json = {"id":self.id,"username":self.username,"role":self.role}
		return json
class group:
	def __init__(self, _id, _name, _shift,_desc):
		self.id = _id
		self.name = _name
		self.shift = _shift
		self.desc = _desc
	def __json__(self):
		json={"id":id,"name":name,"shift":shift,"desc":desc}
		return json
class course:
	def __init__(self, _id, _name, _owner):
		self.id = _id
		self.name = _name
		self.owner = _owner
	def __json__(self):
		json={"id":self.id,"name":self.name,"owner":self.owner}
		return json
class task:
	def __init__(self, _id, _courseID, _groupID,_name, _type, _status, _createDate, _expireDate):
		self.id = _id
		self.courseID = _courseID
		self.groupID = _groupID
		self.name = _name
		self.typo = _type
		self.status = _status
		self.createDate = _createDate
		self.expireDate = _expireDate
	def __json__(self):
		json = {"id":id,"courseID":courseID,"groupID":groupID,"name":name,"type":typo,"status":status,"creationDate":createDate,"expireDate":expireDate}
		return json