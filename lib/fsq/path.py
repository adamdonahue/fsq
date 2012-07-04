# fsq -- a python library for manipulating and introspecting FSQ queues
# @author: Matthew Story <matt.story@axialmarket.com>
#
# fsq/construct.py -- provides path construction convenience functions: tmp,
#                     queue, done, fail, down
#
#     fsq is all unicode internally, if you pass in strings,
#     they will be explicitly coerced to unicode.
#
# This software is for POSIX compliant systems only.
import os

from .internal import coerce_unicode
from . import FSQ_QUEUE, FSQ_TMP, FSQ_ROOT, FSQ_DONE, FSQ_DOWN

####### INTERNAL MODULE FUNCTIONS AND ATTRIBUTES #######
def _path(queue, root, extra):
    return os.path.join(coerce_unicode(root), coerce_unicode(queue),
                          coerce_unicode(extra))

####### EXPOSED METHODS #######
def tmp(p_queue, root=FSQ_ROOT, tmp=FSQ_TMP):
    '''Construct a path to the tmp dir for a queue'''
    return _path(p_queue, root, tmp)

def queue(p_queue, root=FSQ_ROOT, queue=FSQ_QUEUE):
    '''Construct a path to the queue dir for a queue'''
    return _path(p_queue, root, queue)

def done(p_queue, root=FSQ_ROOT, done=FSQ_DONE):
    '''Construct a path to the done dir for a queue'''
    return _path(p_queue, root, done)

def down(p_queue, root=FSQ_ROOT, down=FSQ_DOWN):
    '''Construct a path to the down file for a queue'''
    return _path(p_queue, root, down)