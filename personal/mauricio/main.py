from lxml import etree

day = "Monday']/meal/text() | //day[@name='Tuesday"
parser = etree.XMLParser(resolve_entities=False)
tree = etree.parse('menu.xml', parser)
root = tree.getroot()
# query = "//day[@name='"+day+"']/meal/text()"
query = "//day[@name=$theday]/meal/text()"
result = root.xpath(query, theday = day)
print(str(result))

from websocket import create_connection
ws = create_connection("ws://debaser.god.ctf/debaser_progs/auth/exec")
# print ("Sending 'Hello, World'...")
# ws.send("Hello, World")
# print ("Sent")
# print ("Receiving...")
# result =  ws.recv()
# print ("Received" + str(result))
# ws.close()