from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from models import link

# Create your views here.
def scrape(request):
    page = requests.get('https://www.facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')
  

    for link in soup.find_all('a'):
       link_address = link.get('href')
       link_text = link.string

    return render(request,'result.html', {'link_address':link_address})   