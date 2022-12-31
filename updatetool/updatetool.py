#!/usr/bin/env python3.11

import sys, os, argparse, tomllib, json

class UpdateTool:
	def __init__(self):
		super().__init__()

		parser = argparse.ArgumentParser(
			description="Manage modpacks",
			allow_abbrev=True
		)
		subpar = parser.add_subparsers()

		cmd_help = subpar.add_parser("help", help="Show this help message")
		cmd_help.set_defaults(command=parser.print_help)
		cmd_init = subpar.add_parser("init", help="Initialize Updater")
		cmd_init.set_defaults(command=self.init)
		cmd_refresh = subpar.add_parser("refresh", help="Refresh manifest")
		#cmd_refresh.set_defaults(command=self.refresh)

		# print help message if no arguments
		if len(sys.argv) == 1: 
			parser.print_help()
			sys.exit(1)

		args = parser.parse_args()
		
		args.command()

	def init(self):
		if os.path.isfile("pack.toml"):
			if os.path.isfile("modpackinfo.json"):
				if ask("modpackinfo.json already exists, overwrite? [Y/n] ") == False:
					print("Cancelled")
					sys.exit(0)

			with open("pack.toml", "r") as f:
				packwiz = tomllib.loads(f.read())

			with open("modpackinfo.json", "w") as f:
				json.dump(packwiz, f, indent=4)
		else:
			print("No pack.toml found, please run packwiz first.")
			sys.exit(1)

def ask(text):
	answer = input(text)
	if answer.lower() in ["yes", "ye", "y"]:
		return True
	elif answer.lower() in ["no", "n", ""]:
		return False
	else:
		print("Invalid response")
		return ask(text)

if __name__ == "__main__":
	UpdateTool()