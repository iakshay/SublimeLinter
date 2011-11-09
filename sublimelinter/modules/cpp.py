# -*- coding: utf-8 -*-
# cpp.py - sublimelint package for checking cpp files

from c import Linter as CLinter

CONFIG = {
    'language': 'c++',
    'executable': 'clang',
    #'lint_args': ('-xc++', '-fsyntax-only', '-Werror', '-pedantic', '-')
}


class Linter(CLinter):
    def get_lint_args(self, view, code, filename):
        import os.path
        ret = ('-xc++', '-fsyntax-only', '-Werror', '-pedantic',
            '-fdiagnostics-print-source-range-info', '-I{0}'.format(os.path.dirname(filename)), '-')
        return ret
