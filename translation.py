#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'The dog barks.'
	print(' -- Translation -- ')
    print("English: %s >> %s" % (to_translate, translate(to_translate)))
    print("Filipino: %s >> %s" % (to_translate, translate(to_translate, 'tl')))
    print("Cebuano: %s >> %s" % (to_translate, translate(to_translate, 'ceb')))

if __name__ == '__main__':
    main()
