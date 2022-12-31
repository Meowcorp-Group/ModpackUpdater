#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk as ttk
import sys
import urllib.request as req
import json
import os
import argparse

class Updater(tk.Tk):
	def __init__(self):
		super().__init__()
		print("Checking for updates")
		self.title("Modpack Updater")
		self.geometry("300x100")

		frameBar = ttk.Frame(self)
		frameBar.place(anchor=tk.CENTER, relx=0.5, rely=0.3)

		text = ttk.Label(frameBar, text="Checking for updates")
		text.pack()

		bar = ttk.Progressbar(
			frameBar,
			orient="horizontal",
			length=200,
			mode="indeterminate"
		)
		bar.pack()
		bar.start()

		frameActions = ttk.Frame(self)
		btnCancel = ttk.Button(frameActions, text="Cancel", command=lambda: sys.exit(1))
		btnSkip = ttk.Button(frameActions, text="Skip", command=lambda: sys.exit(0))

		frameActions.place(anchor=tk.SE, relx=1.0, rely=1.0, x=-10, y=-10)
		btnCancel.pack(side=tk.RIGHT, padx=5)
		btnSkip.pack(side=tk.RIGHT)

def checkForUpdates():
	# python3 update.py -b <branch> -u <url> -j <java binary> -p <packwiz jar> -f:optional <file>
	# python3 update.py production https://github.com/Meowcorp-Group/MeowcorpSMP-G2/blob/{branch}/packwiz/modpackinfo.json

	parser = argparse.ArgumentParser(
		description="Checks for updates to the modpack and downloads them if necessary"
	)

	parser.add_argument("-b", "--branch", help="The branch to check for updates", required=True)
	parser.add_argument("-u", "--url", help="The url to modpackinfo.json", required=True)
	parser.add_argument("-j", "--java", help="The java binary to use", required=True)
	parser.add_argument("-p", "--packwiz", help="The packwiz jar to use", required=True)
	parser.add_argument("-f", "--file", help="The file to store the manifest in", required=False, default="updater.json")

	args = parser.parse_args()
	
	url = args.url.format(branch=args.branch)
	file = args.file
	print(url)

	with req.urlopen(url) as response:
		dataRemote = json.loads(response.read())

	if os.path.isfile(file):
		with open(file, "r") as f:
			dataLocal = json.load(f)

		with open(file, "w") as f:
			dataLocal = dataRemote
			json.dump(dataRemote, f, indent=4)
	else:
		with open(file, "w") as f:
			dataLocal = dataRemote
			json.dump(dataRemote, f, indent=4)

	

if __name__ == "__main__":
	app = Updater()
	checkForUpdates()
	app.mainloop()