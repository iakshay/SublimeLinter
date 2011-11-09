# -*- coding: utf-8 -*-
# cpp.py - sublimelint package for checking cpp files

import re

from base_linter import BaseLinter

CONFIG = {
    'language': 'cpp',
    'executable': 'clang',
    #'lint_args': ('-xc++', '-fsyntax-only', '-Werror', '-pedantic', '-')
}


class Linter(BaseLinter):
    def get_lint_args(self, view, code, filename):
        import os.path
        ret = ('-xcpp', '-fsyntax-only', '-Werror', '-pedantic', '-I{0}'.format(os.path.dirname(filename)), '-')
        return ret

    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for line in errors.splitlines():
            match = re.match(r'^.+:(?P<line>\d+):(?P<column>\d+):\s+(?P<error>.+)', line)

            if match:
                error, line = match.group('error'), match.group('line')
                self.add_message(int(line), lines, error, errorMessages)
