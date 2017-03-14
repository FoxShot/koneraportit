#!python

from lxml import html
import requests
import re
import math
from os.path import expanduser
home = expanduser("~")	#multi os support
import urllib
import configparser
#import vlc
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
import os
import mpv
#from mpv import MPV
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#from . Builder import Builder

#class soitin(MPV):
#	def __init__(self, path):
#		super().__init__(window_id=None, debug=False)
#		self.command("loadfile", path, "append")
#		self.set_property("playlist-pos", 0)

#		self.loaded = threading.Event()
#		self.loaded.wait()

class login(requests.Session):
	def __init__(self):
		requests.Session.__init__(self)
		config = configparser.SafeConfigParser()
		configfile = open(home + '/.config/nn-parse/config','r')
		config.readfp(configfile)
		username = config.get("user", "username")
		password = config.get("user", "password")
		payload = {
			"username": username,
			"password": password
		}
		login_url = "http://naurunappula.com/login.php?ref=%2F"
		result = self.post(
			login_url,
			data = payload,
			headers = dict(referer=login_url)
		)
	
	def hae(self, url):
		return self.get(
			url,
			headers = dict(referer = url)
		)

class parseVideos:
	def __init__(self):
		self.url = 'http://naurunappula.com/videot'
#		page = requests.get(self.url)
#		tree = html.fromstring(page.content)
		mie = login()
#		result = mie.get(
#			self.url,
#			headers = dict(referer = self.url)
#		)
		result = mie.hae(self.url)
		tree = html.fromstring(result.content)
		self.names = tree.xpath('//table[@class="padd gridlist"]/tr/td/a[not(text())] | //table[@class="padd gridlist"]/tr/td/a/text()')	#ottaa tyhjät mukaan, mutta antaa objectin
#		self.names = tree.xpath('//table[@class="padd gridlist"]/tr/td/a/text()') #jättää pois tyhjät :(
		self.links = tree.xpath('//table[@class="padd gridlist"]/tr/td/a[@title]/@href')
		self.images = tree.xpath('//table[@class="padd gridlist"]/tr/td/a[@title]/img/@src')
				
def display(video):
#	page = requests.get(video)
#	tree = html.fromstring(page.content)
	tree = html.parse(video)
	video = tree.xpath('//div[@id="viewbody_container"]/div[@id="viewbody"]/div[@id="viewembedded"]/script//text()')
	url = re.search('http:.+[.]flv', video[0])
	return url.group(0)

		
class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
        
		grid = Gtk.Grid()
		self.add(grid)
	
		NN = parseVideos()
#		self.player = mpv.MPV(ytdl=True)
#		self.insta = vlc.Instance()
#		self.player = insta.media_player_new()
	
		i=0
		for vid in NN.images:
			youtube="http://gooby.naurunappula.com/images/icons/youtube.gif"
			video="http://gooby.naurunappula.com/images/icons/video.gif"
			if vid == youtube:
				imgname="youtube.gif"
				
			elif vid == video:
				imgname="video.gif"
				
			else:
				imgname=NN.names[i]+".jpg"
						
			if not os.path.isfile("./"+imgname):				
				response=urllib.request.urlopen(vid)
				with open(imgname, 'wb') as img:
					img.write(response.read())
			
			image=Gtk.Image()
			pb = Pixbuf.new_from_file(imgname)
			image.set_from_pixbuf(pb)

			button = Gtk.Button()
			button.Label = str(i)
			button.Mnemonic = NN.url + NN.links[i]
			button.add(image)
			button.connect("clicked", self.on_button_clicked)
			grid.attach(button,(i%5)+1,math.floor(i/5)+1,1,1)
			i+=1

	def on_button_clicked(self, widget):
#		os.system("cvlc " + display(widget.Mnemonic))
		video = self.insta.media_new(display(widget.Mnemonic))
		video.get_mrl()
		self.player.set_media(video)
		player.play()
#		os.system("mpv " + display(widget.Mnemonic))
#		self.player.play(display(widget.Mnemonic))
#		self.player.wait_for_playback()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
