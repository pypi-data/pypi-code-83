#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    MusaMusa-AnnotatedText Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of MusaMusa-AnnotatedText.
#    MusaMusa-AnnotatedText is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MusaMusa-AnnotatedText is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with MusaMusa-AnnotatedText.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
   MusaMusa-AnnotatedText project : musamusa_atext/annotatedtext.py

   AnnotatedText object allows to store pairs of (textref, AnnotatedString) and
   to yield over with sorted textrefs.

   See the main documentation for more explanations.

   ____________________________________________________________________________

   CONSTANT:
   o  DEFAULT_OPTIONS

   CLASS:
   o  AnnotatedText class
"""
import copy
import importlib

from musamusa_errors.error_messages import ListOfErrorMessages, MusaMusaError
from musamusa_textref.semisortedtextrefsdict import SemiSortedTextRefsDict

from musamusa_atext.annotatedstring import AnnotatedString
from musamusa_atext.annotatedstring import DEFAULT_OPTIONS as ASTRING__DEFAULT_OPTIONS
from musamusa_atext.annotatedstring import PARSINGTOOLS as ASTRING__PARSINGTOOLS

# (pimydoc)AnnotatedText.options
# ⋅A dict (str:...) modifying the way AnnotatedText.__init__() and AnnotatedText.add()
# ⋅work.
# ⋅
# ⋅o  "TextRef class": (str)class name used by AnnotatedStrings objects
# ⋅                    special format: "module.submodule.subsubmodule:classname"
# ⋅                    e.g. "musamusa_textref.textrefdefault:TextRefDefault"
# ⋅                    see "TextRef class(type)"
# ⋅
# ⋅o  "TextRef class(type)": (None|type)
# ⋅                          type of the class used by AnnotatedStrings objects
# ⋅                          Automatically derived by AnnotatedText.__init__()
# ⋅                          from "TextRef class"
# ⋅
# ⋅o  "AnnotatedString:options": copy.deepcopy(ASTRING__DEFAULT_OPTIONS)
# ⋅                              see format in annotatedstring.py
# ⋅
# ⋅o  "AnnotatedString:parsingtools": copy.deepcopy(ASTRING__PARSINGTOOLS)
# ⋅                                   see format in annotatedstring.py
DEFAULT_OPTIONS = {
    "TextRef class": "musamusa_textref.textrefdefault:TextRefDefault",
    "TextRef class(type)": None,
    "AnnotatedString:options": copy.deepcopy(ASTRING__DEFAULT_OPTIONS),
    "AnnotatedString:parsingtools": copy.deepcopy(ASTRING__PARSINGTOOLS),
    }


class AnnotatedText:
    """
        AnnotatedText class

        Use this class to store pairs of (TextRef, AnnotatedString).
        _______________________________________________________________________

        METHODS:
        o  __init__(self, options=None)
        o  add_str(self, textref_str, text_str)
        o  improved_str(self, rightpadding=True)
    """
    def __init__(self,
                 options=None):
        """
            AnnotatedText.__init__()
            ___________________________________________________________________

            ARGUMENT:
            o  options (None or dict, see DEFAULT_OPTIONS)

               (pimydoc)AnnotatedText.options
               ⋅A dict (str:...) modifying the way AnnotatedText.__init__() and AnnotatedText.add()
               ⋅work.
               ⋅
               ⋅o  "TextRef class": (str)class name used by AnnotatedStrings objects
               ⋅                    special format: "module.submodule.subsubmodule:classname"
               ⋅                    e.g. "musamusa_textref.textrefdefault:TextRefDefault"
               ⋅                    see "TextRef class(type)"
               ⋅
               ⋅o  "TextRef class(type)": (None|type)
               ⋅                          type of the class used by AnnotatedStrings objects
               ⋅                          Automatically derived by AnnotatedText.__init__()
               ⋅                          from "TextRef class"
               ⋅
               ⋅o  "AnnotatedString:options": copy.deepcopy(ASTRING__DEFAULT_OPTIONS)
               ⋅                              see format in annotatedstring.py
               ⋅
               ⋅o  "AnnotatedString:parsingtools": copy.deepcopy(ASTRING__PARSINGTOOLS)
               ⋅                                   see format in annotatedstring.py
        """
        self.errors = ListOfErrorMessages()

        self.options = copy.deepcopy(DEFAULT_OPTIONS)
        if options:
            self.options.update(options)

        module, classname = self.options["TextRef class"].split(":")
        try:
            self.options["TextRef class(type)"] = getattr(importlib.import_module(module),
                                                          classname)
        except AttributeError as err:
            # (pimydoc)error::ANNOTATEDTEXT-ERRORID012
            # ⋅Can't create an AnnotatedText object due to the unknown type stored in
            # ⋅options['TextRef class(type)']. This value is itself computed from
            # ⋅self.options["TextRef class"] .
            error = MusaMusaError()
            error.msgid = "ANNOTATEDTEXT-ERRORID012"
            error.msg = "Can't create AnnotatedText from given options " \
                f"since options['TextRef class(type)'] is " \
                f"'{self.options['TextRef class(type)']}' " \
                f"an unknown type. Python error is '{err}'. " \
                f"self.options['TextRef class'] is equal to {self.options['TextRef class']}."
            self.errors.append(error)
            return

        self.annotatedstrings = SemiSortedTextRefsDict(
            textrefclass=self.options["TextRef class(type)"])

    def add_str(self,
                textref_str,
                text_str):
        """
            AnnotatedText.add_str()

            Add a pair of (TextRef, AnnotatedString) to <self>.
            ___________________________________________________________________

            o  textref_str: (str) textual reference
            o  text_str:    (str) text given to the AnnotatedString class

        """
        textref = self.options["TextRef class(type)"]()
        textref.init_from_str(textref_str)

        if textref.errors:
            # (pimydoc)error::ANNOTATEDTEXT-ERRORID010
            # ⋅The call to AnnotatedText.add_str() raised an error due to an incorrect
            # ⋅textual reference.
            error = MusaMusaError()
            error.msgid = "ANNOTATEDTEXT-ERRORID010"
            error.msg = f"Can't add ('{textref_str}', '{text_str}' to this AnnotatedText object " \
                f"since the TextRef object created from '{textref_str}' contains error(s)."
            error.suberrors = textref.errors
            self.errors.append(error)

        if not textref.is_valid:
            # (pimydoc)error::ANNOTATEDTEXT-ERRORID011
            # ⋅The call to AnnotatedText.add_str() raised an error due to an incorrect
            # ⋅textual reference, which is invalid.
            error = MusaMusaError()
            error.msgid = "ANNOTATEDTEXT-ERRORID011"
            error.msg = f"Can't add ('{textref_str}', '{text_str}' to this AnnotatedText object " \
                f"since the TextRef object created from '{textref_str}' is invalid."
            self.errors.append(error)

        astring = AnnotatedString(
            parsingtools=self.options["AnnotatedString:parsingtools"],
            options=self.options["AnnotatedString:options"]).init_from_str(text_str)

        if astring.errors:
            # (pimydoc)error::ANNOTATEDTEXT-ERRORID013
            # ⋅Can't create an AnnotatedText object due to an error in the new AnnotatedString
            # ⋅object.
            error = MusaMusaError()
            error.msgid = "ANNOTATEDTEXT-ERRORID013"
            error.msg = f"Can't add ('{textref_str}', '{text_str}' to this AnnotatedText object " \
                f"since the new AnnotatedText has an error due to the AnnotatedString object."
            error.suberrors = (astring.errors,)
            self.errors.append(error)

        self.annotatedstrings.add(textref, astring)

    def improved_str(self,
                     rightpadding=True):
        """
        TODO
        """
        res = []

        if self.errors:
            res.append("ERROR/WARNINGS:")
            for error in self.errors:
                res.append("* "+str(error.improved_str()))

        astrings = self.annotatedstrings

        if astrings.is_empty():
            res.append("Empty AnnotatedText")
        else:
            res.append(
                f"textrefs={astrings.sorted_textrefs.definition2str()} "
                "(reduced="
                f"{astrings.sorted_textrefs.definition2str(reduced=True, keep_iter_infos=False)})")

            for textref in self.annotatedstrings.sorted_textrefs:
                res.append(f"*  {textref.definition2str()}:"
                           f"\n{astrings.textref2data[textref].improved_str(rightpadding)}")
                res.append("")

        return "\n".join(res)
