#About

PyCharm lets you define live templates that expand a word into a snippet of
code with some input fields. They work similar to textmate snippets and
snipmate for vim.

You can either add your on snippets via File/Settings/Live Templates or select
a region and add the text with Tools/Save as Live Template. 

Live templates are stored in the following location:

	Windows: <your home directory>\.<productname><versionnumber>\config\templates
	Linux: ~\.<product name><version number>\config\templates
	MacOS: ~/Library/Preferences/<product name><version number>/templates

If you have not defined any user templates yet, you can copy the user.xml to
the templates location, otherwise you have to merge the files or add the
templates by hand.

See http://peter-hoffmann.com/2010/python-live-templates-for-pycharm.html for 
more information.
