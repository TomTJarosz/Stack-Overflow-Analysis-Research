import xml.etree.ElementTree as ET
import nntextcleaner as tc
from bs4 import BeautifulSoup as bs
import numpy as np
t_lines=32379999.
links_dic={}
c=0
for line in open('/Users/tommyjarosz/Desktop/posts.xml','r'):
	c+=1
	if c%1000000==0:
		np.save('links_dic_'+str(int(c/1000000)),links_dic)
		links_dic={}
	if c%5000==0:
		print str(100.*c/t_lines) + '% of text read.'
	if 'PostTypeId="2"' in line and 'href' in line:
		root = ET.fromstring(line)
		soup=bs(root.attrib['Body'],'html.parser')
		for l in soup.find_all('a'):
			link= l.get('href')
			if link in links_dic:
				links_dic[link]=links_dic[link]+1
			else:
				links_dic[link]=1
np.save('links_dic_'+str(1+int(c/1000000)),links_dic)
print links_dic
