# tr5-plugin-disabler

A GUI tool for disabling/enabling IK Multimedia T-RackS 5 (TR5) VST3 audio plugins

The T-RackS 5 installer is notorious for installing all the plugins that IK offers, even if you own but a handful of them, cluttering your DAW's plugin list.
This tool will help you to enable only the plugins you own and intend to use.

The tool even remembers the plugins you selected across sessions, such that after you reinstall T-Racks 5 or install a new version, you can simply fire up the tool and restore your previous state with a single click.

<p align="center">
  <img src="https://github.com/opcode81/tr5-plugin-disabler/blob/master/screenshot.jpg?raw=true">
</p>

## Requirements

This script works for VST3 plugins under Windows (with your plugins installed under `%COMMONPROGRAMFILES%\VST3`).

If you do not have Python 3, [download the portable application for Windows](https://github.com/opcode81/tr5-plugin-disabler/releases/download/v1.0.2/tr5_plugin_disabler_v1.0.2_portable_win.zip).

## Usage

* Close any applications using the plugins, e.g. your DAW.
* Start the application.
* Use the checkboxes to enable only the plugins you own/want to use.
* Click apply.

Disabled plugins will simply have the extension ".disabled" added to their filename. All changes are fully reversible.
