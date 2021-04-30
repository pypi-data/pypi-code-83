# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ja_text_cleaner']

package_data = \
{'': ['*']}

install_requires = \
['jaconv>=0.3,<0.4',
 'mojimoji>=0.0.11,<0.0.12',
 'romkan>=0.2.1,<0.3.0',
 'sudachipy>=0.5.2,<0.6.0']

setup_kwargs = {
    'name': 'ja-text-cleaner',
    'version': '0.0.1',
    'description': '日本語のための日本語変換ライブラリ',
    'long_description': '# ja_text_cleaner\n`ja_text_cleaner`は、日本語のための日本語変換ライブラリです。\n\n# パイプライン\n内部処理で使われているライブラリと、主な処理過程の概要を次に示します。\n現在は名前の処理にマッチするように設計されています。\n\n## わかち書き\n1. 制御文字・記号等のノイズを除去\n2. 形態素解析でわかち書き（sudachi）\n\n## 読みがな取得\n1. わかち書きされたトークンの読み（全角カタカナ）を取得（sudachi）\n2. 辞書にヒットしない英字の読み（全角カタカナ）を取得（romkan）\n3. 辞書にヒットしない半角カタカナを全角カタカナに変換（jaconv）\n\n## その他\n1. 必要に応じて半角を全角に変換（mojimoji）\n2. 必要に応じてカタカナからひらがな・ヘボン式に変換（romkan）\n\n\n\n# システム要件\n\n- Python 3.8+\n\n# インストール\n`ja_text_cleaner`のほかに、形態素解析（sudachi）で使用する辞書（sudachidict_core）が必要です。\n\n``` shell\npip install ja_text_cleaner sudachidict_core\n```\n\n# 始める\n\n\n``` Python\nfrom ja_text_cleaner import name\n\n# 制御文字・記号はノイズとして除去されます\nname.Wakachi(" \\t\\n\\xa0a\\u3000-!_")  # "a"\n\n# 形態素解析結果はsudachiの処理結果に依存します\nname.Wakachi("abc123あいうアイウｱｲｳ日本!")  # "abc\u3000123\u3000あ\u3000いう\u3000アイウｱｲｳ\u3000日本"\n\n# CJK互換漢字はCJK統合漢字へ正規化（NFC・NFKC）されません\nname.Wakachi("神")  # "神"\n\nname.Wakachi("日本太郎")  # "日本\u3000太郎"\nname.Zenkaku("日本太郎")  # "日本\u3000太郎"\nname.Katakana("日本太郎")  # "ニッポン\u3000タロウ"\nname.Hiragana("日本太郎")  # "にっぽん\u3000たろう"\nname.Romaji("日本太郎")  # "nippon tarou"\n\nname.Wakachi("nippon tarou")  # "nippon\u3000tarou"\nname.Zenkaku("nippon tarou")  # "ｎｉｐｐｏｎ\u3000ｔａｒｏｕ"\nname.Katakana("nippon tarou")  # "ニッポン\u3000タロウ"\nname.Hiragana("nippon tarou")  # "にっぽん\u3000たろう"\nname.Romaji("nippon tarou")  # "nippon tarou"\n\nname.Wakachi("abc")  # "abc"\nname.Zenkaku("abc")  # "ａｂｃ"\nname.Katakana("abc")  # "エービーシー"\nname.Hiragana("abc")  # "えーびーしー"\nname.Romaji("abc")  # "e-bi-shi-"\n\nname.Wakachi("伊藤")  # "伊藤"\nname.Zenkaku("伊藤")  # "伊藤"\nname.Katakana("伊藤")  # "イトウ"\nname.Hiragana("伊藤")  # "いとう"\nname.Romaji("伊藤")  # "itou"\n\n```\n\n# 注意\n本ライブラリは実験段階です。\n\n',
    'author': 'sasano8',
    'author_email': 'y-sasahara@ys-method.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sasano8/ja_text_cleaner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
