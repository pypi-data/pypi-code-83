# coding=utf-8

import ast
import csv
import re
import sys

MARGIN_WIDTH = 2


def handle(args):
    if args.matrix is not None:
        literal = args.matrix
    elif args.file.name.endswith('.csv'):
        reader = csv.reader(args.file)
        matrix = []
        for row in reader:
            matrix.append(row)
        print_matrix(matrix, args.row_span)
        return
    else:
        literal = args.file.read()
    matrix = ast.literal_eval(literal)
    print_matrix(matrix, args.row_span)


def print_matrix(matrix, row_span):
    widths = []
    for head in matrix[0]:
        widths.append(_width(head))
    row_count = len(matrix)
    col_count = len(widths)
    for row in matrix:
        for j in range(0, len(row)):
            if _width(row[j]) > widths[j]:
                widths[j] = _width(row[j])

    # head
    sys.stdout.write('┌')
    sys.stdout.write('─' * (MARGIN_WIDTH * 2 + widths[0]))
    for j in range(1, col_count):
        sys.stdout.write('┬')
        sys.stdout.write('─' * (MARGIN_WIDTH * 2 + widths[j]))
    sys.stdout.write('┐\n')

    # data lines
    for i in range(0, row_count):
        for j in range(0, col_count):
            item = ''
            if j < len(matrix[i]):
                item = str(matrix[i][j])
            sys.stdout.write('│')
            sys.stdout.write(' ' * MARGIN_WIDTH)
            sys.stdout.write(item)
            sys.stdout.write(' ' * (widths[j] - _width(item) + MARGIN_WIDTH))
        sys.stdout.write('│\n')
        if i == row_count - 1 or row_span == 'none':
            continue
        if row_span == 'all' or (row_span == 'head' and i == 0):
            _print_span(widths)

    # tail
    sys.stdout.write('└')
    sys.stdout.write('─' * (MARGIN_WIDTH * 2 + widths[0]))
    for j in range(1, col_count):
        sys.stdout.write('┴')
        sys.stdout.write('─' * (MARGIN_WIDTH * 2 + widths[j]))
    sys.stdout.write('┘\n')
    sys.stdout.flush()


def _width(content):
    content = str(content)
    count = len(re.findall(r'[\u4e00-\u9fa5]', content))
    return len(content.encode('utf-8')) - count


def _print_span(widths):
    sys.stdout.write('├')
    sys.stdout.write('─' * (MARGIN_WIDTH * 2 + widths[0]))
    for i in range(1, len(widths)):
        sys.stdout.write('┼')
        sys.stdout.write('─' * (MARGIN_WIDTH * 2 + widths[i]))
    sys.stdout.write('┤\n')
