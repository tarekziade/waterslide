# -*- coding: utf-8 -*-
import re
import sys
from docutils import core, nodes
from docutils.parsers.rst import directives, Directive

from docutils.parsers.rst.roles import register_canonical_role
from docutils.nodes import strong


def _style_role(class_, content, text):
    content = '<span class="%s">%s</span>' % (class_, text)
    return [nodes.raw('', content, format='html')], []


def centered_role(role, rawtext, text, lineno, inliner,
                  options={}, content=[]):
    content = '<span class="centered">%s</span>' % text
    return [nodes.raw('', content, format='html')], []

register_canonical_role('centered', centered_role)

def emphasis_role(role, rawtext, text, lineno, inliner,
                  options={}, content=[]):
    content = '<span class="emphasis">%s</span>' % text
    return [nodes.raw('', content, format='html')], []

register_canonical_role('emphasis', emphasis_role)

def subtitle_role(role, rawtext, text, lineno, inliner,
                   options={}, content=[]):

    content = '<span class="subtitle">%s</span><br/>' % text
    return [nodes.raw('', content, format='html')], []

register_canonical_role('subtitle', subtitle_role)


def br_role(role, rawtext, text, lineno, inliner,
       options={}, content=[]):
    return [nodes.raw('', text + '<br/>', format='html')], []

register_canonical_role('br', br_role)

class CenteredText(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    def run(self):
        self.assert_has_content()
        content = '<br/>'.join(self.content)
        args = {'noclasses': False}
        content = '<span class="centered">%s</span>' % content
        return [nodes.raw('', content, format='html')]

directives.register_directive('centered', CenteredText)

