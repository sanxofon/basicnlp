#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging,re
from subprocess import check_output, CalledProcessError, Popen, PIPE

binary = None

logger = logging.getLogger(__name__)


def find_binary():
    try:
        if os.name == 'nt':
            return check_output(['which', 'analyzer.bat']).split()[0]
        else:
            return check_output(['which', 'analyze']).split()[0]
    except (CalledProcessError, KeyError):
        return None


class Analyzer(object):
    def __init__(self, *args, **kwargs):
        self.config = kwargs.get('config', 'analyzer.cfg')
        self.lang = kwargs.get('lang', 'en')
        self.timeout = kwargs.get('timeout', 30)
        self.binary = find_binary()

    def run(self, input, *args, **kwargs):
        cmd = self._build_cmd(*args, **kwargs)
        logger.debug(cmd)
        proc = Popen(cmd, stdin=PIPE, stdout=PIPE)
        outs, errs = proc.communicate(input)
        if errs is None:
            outs = re.sub(r'\n', '', outs) # Clean br
            outs = re.sub(r'\} *\{', '},{', outs) # RESOLVE ERROR HACK
            # Compress json
            outs = re.sub(r'  +', ' ', outs)
            outs = re.sub(r' ?([\[\]\{\}]) ?', r'\1', outs)
            outs = re.sub(r'" ?([\:,]) ?', r'"\1', outs)
            return '{"sentences":['+outs+']}'
            # return outs
        else:
            raise Exception(errs)

    def _build_param(self, key, val):
        return '--{}'.format(key), val

    def _build_flag(self, a):
        return '--{}'.format(a)

    def _build_cmd(self, *flags, **kwargs):
        cmd = [self.binary, '-f', self.config]

        for f in flags:
            flag = self._build_flag(f)
            if flag:
                cmd.append(flag)

        for key, val in iter(kwargs.items()):
            param, value = self._build_param(key, val)
            cmd += [param, value]

        cmd += ['--output', 'json']
        return cmd
