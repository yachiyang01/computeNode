class Node:
	def __init__(self,fid,no,time,typeid,totalEX,owner):
		self.fid = fid
		self.no = no
		self.time = time
		self.type = typeid # typeid=1 means cpu typeid=2 means gpu
		self.totalEX = totalEX
		self.owner = owner
		self.next = None # the pointer initially points to nothing
	def info(self):
		print("ID:",self.fid);
		print("No:",self.no);
		print("Execution Time:",self.time);
		print("Compute Device:",self.type);
		print("Total Ex Time:",self.totalEX);
		print("Application From:",self.owner);
		print("Next ID",self.next)

	def next(self,fid):
		self.next=fid
#node1 = Node(1,1,3.1415,1,29998,'A') 
#node2 = Node(2,1,2.56,2,29998,'A')
#node1.next = node2 # 12->99
#print(node1.time)
#print(node2.fid)
#node1.info();

