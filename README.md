# tr5-plugin-disabler

A GUI utility for disabling/enabling IK Multimedia T-RackS 5 (TR5) VST3 audio plugins

The T-RackS 5 installer is notorious for installing all the plugins that IK offers, even if you have but a handful of them, cluttering your DAW's plugin list.
This utility will help you to enable only the plugins you own and intend to use.

The utility even remember the plugins you had previously selected after you reinstall T-Racks 5 or install a new version, such that you can restore your previous state with a single click.

## Requirements

This script works for VST3 plugins under Windows (with your plugins installed under `%COMMONPROGRAMFILES%\VST3`).

## Usage

* Close your DAW (and any other programs using the plugins).
* Run the script.
* Enable/disable plugins using the checkboxes.
* Click apply.

Disabled plugins will simply have the extension ".disabled" added to their filename. All changes are fully reversible.
