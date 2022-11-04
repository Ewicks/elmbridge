from random_user_agent.user_agent import UserAgent
import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import re
import time
from .models import *
from .forms import *
from torpy.http.requests import TorRequests
import requests
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


# def hold(request):


def interface(request):
	words = Word.objects.all()
	form = WordForm()
	dateform = DateForm()

	if request.method == 'POST':
		print(request.POST)
		form = WordForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('interface')

	context = {
		'form': form,
		'words': words,
		'dateform': dateform,

	}
	return render(request, 'tasks/interface.html', context)


def deleteword(request, pk):
	word = Word.objects.get(id=pk)

	if request.method == 'POST':
		word.delete()
		return redirect('interface')

	return render(request, 'tasks/delete.html', {})


wordslist = []


def index(request):

	context = {}
	return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

# def deleteTask(request, pk):
# 	item = Task.objects.get(id=pk)

# 	if request.method == 'POST':
# 		item.delete()
# 		return redirect('/')

# 	context = {'item': item}
# 	return render(request, 'tasks/delete.html', context)


def test(request):
	return render(request, 'tasks/test.html', {})


def my_view(request):
	
	if request.method == 'POST':
		datesdict = {}
		datesdict = request.POST.dict()
		print(datesdict)
		startdate = datesdict['startdate']
		enddate = datesdict['enddate']
		list = my_function1(startdate, enddate)
		

	return render(request, 'tasks/test.html', {'list': list})

# def my_view(request):
# 	Category.create_from_list()
# 	return render(request, 'tasks/test.html', {})

def get_word_objects():
	words = Word.objects.values_list('word', flat=True)
	objectlist = list(words)
	# for x in words:
	# 	wordslist.append(x)
	return objectlist


def my_function1(startdate, enddate):
	
	wordlist = get_word_objects()
	alldates = pd.date_range(start=f"{startdate}", end=f"{enddate}").strftime("%Y-%m-%d")
	alldateslist = list(alldates)
	print(startdate)
	print(enddate)

	listofdata = []

	for x in alldateslist:
		if x == len(alldateslist):
			return data
			break
		else:
			# print(x, testt)
			code(x, wordlist)

	return data


data = []

def convert(s):
 
    # initialization of string to ""
    new = ""
 
    # traverse in the string
    for x in s:
        new = new + x + '|'
 
    # return string
    return new
     

def code(x, wordlist):

	user_agent_rotator = UserAgent(software_names=['chrome'], operating_systems=['windows', 'linux'])

	# Get Random User Agent String.
	user_agent = user_agent_rotator.get_random_user_agent()

	baseurl = 'https://emaps.elmbridge.gov.uk/ebc_planning.aspx'

	header = {'User-Agent': user_agent}

	b = True

	while b is True:
		try:
			r = requests.get(f'https://emaps.elmbridge.gov.uk/ebc_planning.aspx?pageno=1&template=AdvancedSearchResultsTab.tmplt&requestType=parseTemplate&USRN%3APARAM=&apptype%3APARAM=&status%3APARAM=&decision%3APARAM=&ward%3APARAM=&txt_search%3APARAM=&daterec_from%3APARAM={x}&daterec_to%3APARAM={x}&datedec_from%3APARAM=&datedec_to%3APARAM=&pagerecs=50&orderxyz%3APARAM=REG_DATE_DT%3ADESCENDING&SearchType%3APARAM=Advanced', headers=header, timeout=100)
			soup = BeautifulSoup(r.content, 'lxml')
			houselist = soup.find_all('tr')
			linkslist = []
			# time.sleep(3)

			updatehouselist = []

			addresslist = []
			print(wordlist)
			# Get all house sections that contain keyword in a list
			# modifiedlist = wordlist.replace(",", "|")
			# print(modifiedlist)
			# s = wordslist
			convertedlist = convert(wordlist)
			# print(convertedlist)
			words_search_for = convertedlist.rstrip(convertedlist[-1])
			# print(words_search_for)


			# words_search_for = 'extension|loft|rear|side|double'

			for house in houselist:
				if (house.find('td', string=re.compile((words_search_for), flags=re.I))):
					updatehouselist.append(house)

			for house in updatehouselist:
				address = house.find('td', class_='address')
				addresslist.append(address.get_text())
				for link in house.find_all('a', href=True):
					homepagelinks = link['href']
					linkslist.append(homepagelinks)

			contactlinkslist = []

			for linkkk in linkslist:
				r = requests.get(linkkk, headers=header, timeout=100)
				soup = BeautifulSoup(r.content, 'lxml')
				atags = soup.find('div', id='atPubMenu').find('a')
				parturl = atags['href']
				contacturl = baseurl + parturl
				contactlinkslist.append(contacturl)


			contactnameslist = []



			for linkk in contactlinkslist:
				r = requests.get(linkk, headers=header, timeout=100)
				soup = BeautifulSoup(r.content, 'lxml')
				atags = soup.find('div', class_='atPanelContainer').find('dd').find_next('dd').contents[0]
				contactnameslist.append(atags.get_text())




			# for i, t in enumerate(zip(addresslist, contactnameslist)):
			#     it = (i, t)
			#     data.append(it)



			# testdata = zip(addresslist, contactnameslist)


			zippeddata = zip(addresslist, contactnameslist)
			for zipp in zippeddata:
				data.append(zipp)
			# print(data)
			b = False

			
			# if close == False:
			# 	return data
			# 	variablee = False
			# 	break
			# else:
			# 	continue
			# for x in testdata:
			#     data.append(x)

			# newdata = tuple(data)
			# for data in newdata:
			#     print(data[0])
			#     print(data[1])

			
		except:
			print('try again')
			# time.sleep(random.randint(1, 10))
			time.sleep(2)
			b = True

# def returnlist(list):
# 	return list
	