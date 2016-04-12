import os
import csv
import requests
from unidecode import unidecode
from bs4 import BeautifulSoup
import math
csv_columns = ["url","name","img","newprice",  "oldprice","category","brand"]
currentPath = os.getcwd()
csv_file = "even.csv"
j=0
def WriteDictToCSV(data):
	global csv_columns
	global csv_file
	global j
	try:
		with open(csv_file, 'a+') as csvfile:
			writer = csv.DictWriter(csvfile, delimiter=';', lineterminator='\n', fieldnames=csv_columns)
			if j == 0:
				writer.writeheader()
				j=1
			writer.writerow(data)
		return 1
	except Exception as e:
		print(str(e))
		return 0

# def deep_scrape(url):
# 	try:
# 		url=url+'#specs'
# 		print("\n" + "Deep Scraping Device @: " + url + "\n")
# 		response=requests.get(url)
# 		data=response.content	
# 		soup=BeautifulSoup(data,'html.parser')
# 		specs_div=soup.find('div' , attrs={'id' : 'specs-full'})
# 		name_div=soup.find('h1',attrs={"itemprop":"name"})
# 		name=name_div.text.strip()
# 		print("Name: ")
# 		print(name)

# 		if not specs_div:
# 			specs_div=soup.find('div',attrs={'id' : 'specs-short'})
# 		specs_list=specs_div.find('dl' , attrs={'class' : 'stats'})
# 		specs=specs_list.findAll('dt')
# 		val=specs_list.findAll('dd')
# 		count=0
# 		brand=color=os=os_v=ram=storage=model=comp=""
# 		for spec in specs:
# 			if spec.text.strip()=="Brand":
# 				brand=unicode(val[count].text.strip())
# 				print("Brand: " + brand)
# 			if spec.text.strip()=="Compatible with":
# 			 	comp=unicode(val[count].text.strip())
# 			# if spec.text.strip()=="Color":
# 			# 	color=unicode(val[count].text.strip())
# 			# 	print("Color: " + color)
# 			# if spec.text.strip()=="Operating System":
# 			# 	os=unicode(val[count].text.strip())
# 			# 	print("Operating System: " + os)
# 			# if spec.text.strip()=="Operating System Version":
# 			# 	os_v=unicode(val[count].text.strip())
# 			# 	print("OS Version: " + os_v)
# 			# if spec.text.strip()=="RAM Memory":
# 			# 	ram=unicode(val[count].text.strip())
# 			# 	print("RAM: " + ram)
# 			# if spec.text.strip()=="Storage Capacity":
# 			# 	storage=unicode(val[count].text.strip())
# 			# 	print("Storage: " + storage)
# 			# if spec.text.strip()=="Model Number":
# 			# 	model=unicode(val[count].text.strip())
# 			# 	print("Model: " + model)
# 			# count+=1
# 		try:
# 			#return(brand,color,os,os_v,ram,storage,model,comp)
# 			return(brand,name,comp)
# 		except Exception as e:
# 			print(str(e))
# 			return
# 	except Exception as e: 
# 		print(str(e))
# 		return
	
def getBrand(url,cat):
	print(url)
	response=requests.get(url)
	data = response.content
	soup = BeautifulSoup(data, "html.parser")
	brands=soup.find("dd",attrs={"data-filtertype":"Brand"})
	if not brands:
		getLink(url,cat,"Other")
		return
	brands=brands.findAll("ul")
	brands=brands[0]
	brands=brands.findAll("li")
	for brand in brands:
		b=brand['data-refinement']
		link=brand.findAll("input",attrs={"type":"checkbox"})
		link=link[0]
		link=link['value']
		# try:
		# 	if link.index('action'):
		# 		link=link[:link.index("action")]
		# except Exception as e:
		# 	# print(str(e))
		link=link.strip('?')
		getLink(link,cat,b)
	

def get_scrape(url,text,brand,page):
	try:
		print(url)
		no_of_pages=0
		response = requests.get(url)
		data = response.content
		soup = BeautifulSoup(data, "html.parser")
		data=list()
		list_thumb = soup.findAll("div" , attrs={'class':'placard'})
		#print(list_thumb)
		for product in list_thumb:
			print("On Page No. : " + page)
			image_div =product.find("div" , attrs={"class":"small-5"})
			if not image_div:
				image_div=product.findAll("div", attrs={"class":"small-12"})
				image_div=image_div[0]
			name_div=product.findAll("div", attrs={"class": "row"})
			name_div=name_div[0]
			name=name_div.findAll("a",attrs={"class":"itemLink"})
			url=name[0]['href']
			name=name[0]['title']
			details_div=product.find("div" , attrs={"class":"small-7"})
			image=names=oldprice=newprice=""
			if image_div:
				image=image_div.find("img")
			if not details_div:
				details_div=product.findAll("div",attrs={"class":"small-12"})
				details_div=details_div[1]
			oldprice = details_div.find("span" , attrs= {'class':'was'})
			newprice = details_div.find("span" , attrs= {'class':'is'})
			if not oldprice or oldprice.text=="":
				oldprice=newprice
			#color,os,os_v,ram,storage,model,comp=deep_scrape(name['href'])
			var={}
			try:
				if image.get('data-src'):
					var['img']=unidecode(image['data-src'])
				else:
					var['img']=unidecode(image['src'])
				var['name'] = unidecode(name.strip())
				print("name: " + name)
				var['url']=unidecode(url)
				var['oldprice']=unidecode(oldprice.text.strip())
				var['newprice']=unidecode(newprice.text.strip())
				var ['category']=unidecode(text)
				var['brand']=unidecode(brand)
				# var['brand']=unidecode(brand)
				# var['color']=unidecode(color)
				# var['os']=unidecode(os)
				# var['os_version']=unidecode(os_v)
				# var['ram']=unidecode(ram)
				# var['storage']=unidecode(storage)
				# var['model_number']=unidecode(model)
				# var['compatible_with']=unidecode(comp)
				#print(var)
				WriteDictToCSV(var)
			except Exception as e:
				print(str(e))
				
	except Exception as e:
		print(str(e))
		return
	
	
def getLink(url,cat,brand):
	try:
		print("scapping for brand:")
		print(brand)
		print("Brand url: ")
		print(url)
		no_of_pages=0
		response = requests.get(url)
		data = response.content
		soup = BeautifulSoup(data, "html.parser")
		link=soup.find('div', attrs={'class' : 'listing-page-text'})
		if link:
			link=unidecode(link.text.strip())
			try:
				results=float(link.split(" ")[0])
				print("Total results : ")
				print(results)
				no_of_pages =math.ceil(results/15)
				print("No. of pages : ")
				print(no_of_pages)
			except Exception as e:
				print(str(e))
				return
			count=0
			while(no_of_pages>0):
				count=count+1
				no_of_pages-=1
				print("On Page No. : ")
				print(count)
				get_scrape(url+'&page='+str(count),cat,brand,str(count))
		else:
			return
	except Exception as e:
		print(str(e))
		return

		
	# 	count=0
	# 	while (no_of_pages > 0): 
	# 		count=count + 1
	# 		no_of_pages=no_of_pages - 1
	# 		print("On page no. : ")
	# 		print(count)
	# 		get_scrape(url+'&page='+str(count) , text,str(count))
				
	# 	return
	# except Exception as e:
	# 	print(str(e))
	# 	return
with open('souq-cat.csv') as csvfile:
	reader=csv.DictReader(csvfile, delimiter=";")
	for row in reader:
		print(row['category'])
		getBrand(row['url'],row['category'])

		
		
