import hy.macros
from hy.core.language import eval, is_none, read_str
hy.macros.require('hy.contrib.walk', None, assignments=[['let', 'let']],
    prefix='')
import logging
import re
from jedhy.api import API
from pygls.lsp.methods import COMPLETION, HOVER, TEXT_DOCUMENT_DID_CHANGE, TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN
from pygls.lsp.types import CompletionItem, CompletionList, CompletionOptions, CompletionParams, Hover, MarkupContent, MarkupKind
from pygls.server import LanguageServer
from .jedhy import Jedhy
logger = logging.getLogger('hyls.server')


def cursor_line(ls, uri, ln):
    _hyx_letXUffffX1 = {}
    _hyx_letXUffffX1['doc'] = ls.workspace.get_document(uri)
    _hyx_letXUffffX1['content'] = _hyx_letXUffffX1['doc'].source
    _hyx_letXUffffX1['lines'] = _hyx_letXUffffX1['content'].split('\n')
    return _hyx_letXUffffX1['lines'][ln]


def cursor_word(ls, uri, ln, cn):
    _hyx_letXUffffX2 = {}
    _hyx_letXUffffX2['line'] = cursor_line(ls, uri, ln)
    for m in re.finditer('[\\.\\?\\-\\w]+', _hyx_letXUffffX2['line']):
        if m.start() <= cn and cn <= m.end():
            return _hyx_letXUffffX2['line'][m.start():cn:None]
            _hy_anon_var_2 = None
        else:
            _hy_anon_var_2 = None


def cursor_word_all(ls, uri, ln, cn):
    _hyx_letXUffffX3 = {}
    _hyx_letXUffffX3['line'] = cursor_line(ls, uri, ln)
    for m in re.finditer('[\\.\\?\\-\\w]+', _hyx_letXUffffX3['line']):
        if m.start() <= cn and cn <= m.end():
            return _hyx_letXUffffX3['line'][m.start():m.end():None]
            _hy_anon_var_4 = None
        else:
            _hy_anon_var_4 = None


class Server:

    def __init__(self):
        self.server = LanguageServer()
        self.jedhy = Jedhy(API(), logger=logger)
        self.imports = []

        @self.server.feature(COMPLETION, CompletionOptions(
            trigger_characters=['.']))
        def completions(params):
            _hyx_letXUffffX4 = {}
            _hyx_letXUffffX4['word'] = cursor_word(self.server, params.
                text_document.uri, params.position.line, params.position.
                character)
            complist = CompletionList(is_incomplete=False, items=[])
            if not is_none(_hyx_letXUffffX4['word']):
                for candidate in self.jedhy.complete(_hyx_letXUffffX4['word']):
                    complist.add_item(CompletionItem(label=candidate))
                _hy_anon_var_6 = None
            else:
                _hy_anon_var_6 = None
            return complist

        @self.server.feature(HOVER)
        def hover(params):
            _hyx_letXUffffX5 = {}
            _hyx_letXUffffX5['word'] = cursor_word_all(self.server, params.
                text_document.uri, params.position.line, params.position.
                character)
            if not is_none(_hyx_letXUffffX5['word']):
                _hyx_letXUffffX6 = {}
                _hyx_letXUffffX6['docs'] = self.jedhy.docs(_hyx_letXUffffX5
                    ['word'])
                _hy_anon_var_8 = Hover(contents=MarkupContent(kind=
                    MarkupKind.PlainText, value=_hyx_letXUffffX6['docs'])
                    ) if _hyx_letXUffffX6['docs'] != '' else None
            else:
                _hy_anon_var_8 = None
            return _hy_anon_var_8

        @self.server.feature(TEXT_DOCUMENT_DID_OPEN)
        def did_open(params):
            self.imports = []
            self.find_and_eval_imports(self.server, params.text_document.uri)
            return self.jedhy.refresh_ns(self.imports)

        @self.server.feature(TEXT_DOCUMENT_DID_CLOSE)
        def did_close(params):
            self.imports = []

        @self.server.feature(TEXT_DOCUMENT_DID_CHANGE)
        def did_change(params):
            return None
        return None

    def find_and_eval_imports(self, ls, uri):
        _hyx_letXUffffX7 = {}
        _hyx_letXUffffX7['doc'] = ls.workspace.get_document(uri)
        for m in re.finditer(
            '\\(\\s*(import|require)\\s+([\\w\\.]+|\\[[\\w\\.\\s\\*\\?:\\[\\]]+\\])\\)'
            , _hyx_letXUffffX7['doc'].source):
            logger.info('try to evaluate: ' + m.group())
            try:
                eval(read_str(m.group()))
            except BaseException as e:
                _hy_anon_var_14 = logger.info('cannot evaluate: ' + repr(e))
            else:
                _hy_anon_var_14 = self.imports.append(m.group())

    def start(self):
        return self.server.start_io()

