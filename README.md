# ModpackUpdater
python modpack management tool that works with packwiz

This project should run out of the box without any additional dependencies, as long as you are using the latest versions of python.

## Installation
### Updater
Updater is designed for MultiMC-based launchers. We reccomend [Prism Launcher](https://prismlauncher.org/).

- Place `updater-bootstrap.py` in the `.minecraft` folder of your instance. 
- Download the latest packwiz installer bootstrap jar, and place it in the same directory as Updater.
- Go to Edit Instance, Settings, Custom Commands, Pre-launch command, and enter:
  ```sh
  python updater-bootstrap.py
  ```
  - For maximum compatibility, call python with `python` instead of `python3` (because Windows)

### UpdateTool
- Place `updatetool.py` in your project directory.
- Optional: Rename to `updatetool` for shorter commands.
- Download the latest packwiz CLI build for your platform, and place it in the same directory as UpdateTool
- Updating:
  - Update UpdateTool with `./updatetool upgrade updatetool`
  - Update packwiz CLI with `./updatetool upgrade packwiz`
  - Update both with `./updatetool upgrade`

## Usage
### Updater
Updater should run when the instance is run, and will update itself automatically if an update is available.

### UpdateTool

## License
ModpackUpdater - python modpack management tool that works with packwiz <br>
Copyright (C) 2022 Meowcorp-Group

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
