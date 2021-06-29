import os
import pickle
import tkinter as tk
from typing import Dict

VST3_PATH = os.path.join(os.getenv("COMMONPROGRAMFILES"), "VST3")
EXT_ENABLED = ".vst3"
EXT_DISABLED = ".vst3.disabled"
CONFIG_FILE = "tr5_plugin_disabler.pickle"


def find_tr5_plugins() -> Dict[str, bool]:
    d = {}
    for fn in os.listdir(VST3_PATH):
        if fn.startswith("TR5 "):
            if fn.endswith(EXT_ENABLED):
                plugin = fn.replace(EXT_ENABLED, "")
                d[plugin] = True
            elif fn.endswith(EXT_DISABLED):
                plugin = fn.replace(EXT_DISABLED, "")
                d[plugin] = False
    return d


class TR5PluginDisablerGui(tk.Frame):
    def __init__(self, plugins_on_disk: Dict[str, bool], plugins_user_config: Dict[str, bool], master=None):
        super().__init__(master)
        self.plugins_on_disk = plugins_on_disk
        self.master = master
        self.pack()

        plugin_frame = tk.Frame(self)
        plugin_vars = {}
        for i, (plugin, enabled) in enumerate(sorted(plugins_user_config.items())):
            var = tk.IntVar(value=int(enabled))
            checkbox = tk.Checkbutton(plugin_frame, text=plugin, variable=var)
            checkbox.grid(column=i%3, row=i//3, sticky=tk.W)
            plugin_vars[plugin] = var
        self.plugin_vars = plugin_vars
        plugin_frame.pack()

        tk.Button(self, command=self.apply, text="   Apply   ").pack()

    def apply(self):
        plugins_user_config = {}
        for plugin, var in self.plugin_vars.items():
            if plugin not in self.plugins_on_disk:
                continue
            current_state_enabled = self.plugins_on_disk[plugin]
            desired_state_enabled = var.get() > 0
            plugins_user_config[plugin] = desired_state_enabled
            if current_state_enabled != desired_state_enabled:
                current_ext = EXT_ENABLED if current_state_enabled else EXT_DISABLED
                desired_ext = EXT_ENABLED if desired_state_enabled else EXT_DISABLED
                print(f"{plugin}: {current_state_enabled} -> {desired_state_enabled}")
                os.rename(os.path.join(VST3_PATH, plugin + current_ext), os.path.join(VST3_PATH, plugin + desired_ext))
        with open(CONFIG_FILE, "wb") as f:
            pickle.dump(plugins_user_config, f)
        self.master.destroy()


if __name__ == '__main__':
    plugins_on_disk = find_tr5_plugins()
    plugins_user_config = plugins_on_disk.copy()
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "rb") as f:
            plugins_user_config.update(pickle.load(f))
    root = tk.Tk()
    root.title("T-RackS 5 Plugin Disabler")
    app = TR5PluginDisablerGui(plugins_on_disk, plugins_user_config, master=root)
    app.mainloop()
