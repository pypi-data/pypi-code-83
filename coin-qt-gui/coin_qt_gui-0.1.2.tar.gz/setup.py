#!/usr/bin/env python3
'''
  V0.1.2 - Remover e substituir o arquivo userconf pela biblioteca user_utils
  
'''

from setuptools import setup


DESCRIPTION = 'Vizualizar cotação de criptomoedas'
LONG_DESCRIPTION = 'Obtem cotação, cadastra alertas, converte unidade criptomoedas para Real(R$) do Brasil'

setup(
	name='coin_qt_gui',
	version='0.1.2',
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	author='Bruno Chaves',
	author_email='brunodasill@gmail.com',
	license='MIT',
	packages=['coin_qt_gui'],
	install_requires=['PyQt5', 'user_utils==0.1.1'],
	zip_safe=False,
	url='https://github.com/Brunopvh/coin-qt-gui',
	project_urls = {
		'Código fonte': 'https://github.com/Brunopvh/coin-qt-gui',
		'Download': 'https://github.com/Brunopvh/coin-qt-gui/archive/refs/heads/master.zip'
	},
)

