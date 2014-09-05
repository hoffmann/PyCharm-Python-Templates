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
	
## Example

MacOS, PyCharm 3

```
git clone git@github.com:hoffmann/PyCharm-Python-Templates.git
cp PyCharm-Python-Templates/user.xml ~/Library/Preferences/PyCharm30/templates/
```

You could also copy/paste the template XML to the `Python.xml` file but that's more work.

If you have not defined any user templates yet, you can copy the user.xml to
the templates location, otherwise you have to merge the files or add the
templates by hand.

See http://peter-hoffmann.com/2010/python-live-templates-for-pycharm.html for 
more information.


## How to use

Now you should be able to type "fnpdoc`<TAB>`", meaning you type the letters "fnpdoc" and then press the button `<TAB>` and it will fill the live template, in this case with the numpy docstring template for a function. Visually,

    fnpdoc<TAB>

will become:

    Parameters
    ----------
    
    
    Returns
    -------
    
    
    Raises
    ------
