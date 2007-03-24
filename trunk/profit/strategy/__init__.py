#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2007 Troy Melhase
# Distributed under the terms of the GNU General Public License v2
# Author: Troy Melhase <troy@gci.net>

from PyQt4.QtCore import QObject

from profit.lib import logging
from profit.lib.core import Settings


class Strategy:
    def __init__(self):
        self.threads = []
        self.tickers = []

    @classmethod
    def fromSchema(cls, schema):
        tickers = tickers(schema)
        singleshots = singleshots(schema)
        instance = cls()
        return instance

    def build(self, session):
        tickers = ifitler(self.schema.immediateChildren,
                          lambda x:hasattr(x, 'tickerId'))
        for ticker in tickers:
            ticker.build()
            self.tickers[ticker.tickerId] = ticker

    def execute(self, session):
        """

        It's important to note that runners are called only once:
        after this call is complete, the strategy is running.
        """
        runners = [c for c in self.schema.immediateChildren
                    if hasattr(c, 'exectype')]
        singles = ifilter(runners, lambda x:x.exectype=='singleshot')
        threads = ifilter(runners, lambda x:x.exectype=='periodic')
        handlers = ifilter(runners, lambda x:x.exectype=='messagehandler')

    threadinterval = 1000

    def start_threads(self, callables):
        """
        executes external program, callable object, or callable factory
        callables and factories can access strategy instance
        location inspected for argument names once only at thread start
        location executed on schedule
        """
        for child in self.chidren:
            thread = StrategyThread(child)
            thread.start()
            self.threads.append(thread)

    def execute_singles(self, callables):
        """
        executes external program or callable object once, in instance order
        executes callable factory and factory results once
        callable objects and factories inspected for argument names
        callables and factories can access strategy instance
        """
        for call in callables:
            execute_object_shell_or_factory(call)

    def associate_message_handlers(self):
            """
            callable object or callable factory (never external program)
            location arguments inspected only once when created
            callable object given message to process
            callable factory result object given message to process
            factories (but not callables) can access strategy instance
            """
            for call in self.callables:
                register_callable_for_its_message_types(call)

