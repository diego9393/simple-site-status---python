#!/usr/bin/python
from gi.repository import Gtk

import sys
import os
import urllib

class Ventana:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file("gui.glade")
		self.window = self.builder.get_object("window1")
		self.label = self.builder.get_object("label1")
		self.entry = self.builder.get_object("entry1")
		self.window.show_all()
		# Magia :P
		self.builder.connect_signals(self)

	def onclick1(self, widget):
		self.entry = self.entry.get_text()
		status = "Estado: offline"
		sitecode = urllib.urlopen(self.entry).getcode()
		
		if sitecode == 200:
			status = "Estado: online"
			self.label.set_text(status)
			
if __name__ == "__main__":
	v = Ventana()
	Gtk.main()
