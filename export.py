#!/usr/bin/env python
"""Export Pycharm templates to html"""
import sys
import lxml.etree
import os.path
import cgi


def export(filename):
    tree = lxml.etree.parse(open(filename))
    print '<dl>'
    for template in tree.findall('.//template'):
        print '<dt>%s</dt>' % (cgi.escape(template.get('name')))
        print '<dd>%s\n<pre class="prettyprint">%s\n</pre>\n</dd>\n' %
        (template.get('description'), template.get('value'))
    print '</dl>'


def main(argv=None):
    if argv is None:
        argv = sys.argv

    user_xml_file = os.path.expanduser(
        '~/.PyCharm30/config/templates/user.xml'
    )
    if len(argv) == 2:
        user_xml_file = argv[1]

    export(user_xml_file)

if __name__ == '__main__':
    main()
