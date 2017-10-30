# -*- coding: utf-8 -*-

import types


def space_decorator(func):
	def wrapper(func_arg):
		if isinstance(func_arg, (list, tuple)):
			return type(func_arg)(func(iter(func_arg)))

		if isinstance(func_arg, types.GeneratorType):
			return func(func_arg)

	return wrapper


@space_decorator
def space_cleaning(space_junk):
	prev_item = False
	for item in space_junk:
		if item:
			prev_item = True
			yield item
		elif prev_item:
			nxt = next(space_junk)
			if not nxt:
				pass
			else:
				yield item
				yield nxt
