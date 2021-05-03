#!/usr/bin/env python3

import os
import re
import inquirer


def create_matrix(string: str):
  lines = string.splitlines()
  return [re.split('(\t+)+', line) for line in lines]


def remove_tabs(matrix: list):
  for i in range(len(matrix)):
    line = matrix[i]
    matrix[i] = [x for x in line if '\t' not in x]
  return matrix


def parse_inquirer_questions(matrix):
  return [
      inquirer.List('issue_name',
                    message="What issue do you wish to checkout?",
                    choices=[x[2] for x in matrix],
                    carousel=False
                    ),
      inquirer.Confirm('upstream',
                       message="Add the branch to the upstream remote?"),
  ]


def parse_branch_name(matrix, issue_name) -> str:
  row = [row for row in matrix if issue_name in row][0]
  return {
      'human_readable': f'issue-#{row[0]}-{row[2]}',
      'git_readable': f'issue-\#{row[0]}-{row[2]}'
  }


def main():
  list_output = os.popen('gh issue list | cat').read()
  matrix = create_matrix(list_output)
  matrix = remove_tabs(matrix)
  questions = parse_inquirer_questions(matrix)

  answers = inquirer.prompt(questions)
  branch_names = parse_branch_name(
      matrix, answers['issue_name'])

  os.popen(f"git checkout -b {branch_names['human_readable']}")

  if answers['upstream']:
    os.popen(f"git push -u origin {branch_names['git_readable']}")
