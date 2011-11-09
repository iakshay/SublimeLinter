# -*- coding: utf-8 -*-
# c.py - sublimelint package for checking c files

import re

from base_linter import BaseLinter

CONFIG = {
    'language': 'c',
    'executable': 'clang',
    #'lint_args': ('-xc', '-fsyntax-only', '-std=c99', '-Werror', '-pedantic', '-')
}


class Linter(BaseLinter):
    def get_lint_args(self, view, code, filename):
        import os.path
        ret = ('-xc', '-fsyntax-only', '-std=c99', '-Werror', '-pedantic',
            '-fdiagnostics-print-source-range-info', '-I{0}'.format(os.path.dirname(filename)), '-')
        return ret

    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for line in errors.splitlines():
            match = re.match(r'^.+:(?P<line>\d+):(?P<column>\d+):(?:(?P<ranges>[{}0-9:\-]+):)?\s+(?P<error>.+)', line)
            if match:
                error, line, ranges = match.group('error'), match.group('line'), match.group('ranges')
                if ranges:
                    for ra in re.finditer(r'{(?P<sline>\d+):(?P<scol>\d+)-(?P<eline>\d+):(?P<ecol>\d+)}', ranges):
                        sline, scol, eline, ecol = int(ra.group('sline')), int(ra.group('scol')), int(ra.group('eline')), int(ra.group('ecol'))
                        #underline_range(self, view, lineno, position, underlines, length=1)
                        self.underline_range(view, sline, scol - 1, errorUnderlines, ecol - scol)
                self.add_message(int(line), lines, error, errorMessages)
