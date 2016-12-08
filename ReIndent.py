import sublime, sublime_plugin
class ReIndentToSpaceTwoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('set_setting', {"setting": "tab_size", "value": 2})
		self.view.run_command('expand_tabs')

class ReIndentToTabFourCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('unexpand_tabs')
		self.view.run_command('set_setting', {"setting": "tab_size", "value": 4})
