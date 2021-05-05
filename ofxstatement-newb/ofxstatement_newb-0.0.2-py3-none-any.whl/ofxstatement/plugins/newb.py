import csv
from typing import Iterable

from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import Statement, StatementLine, BankAccount, recalculate_balance, generate_unique_transaction_id, generate_transaction_id


class NewBCsv():
    delimiter = ';'
    quotechar = '"'
    escapechar = None
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = csv.QUOTE_ALL

class NewBPlugin(Plugin):
    """NewB (Belgian Cooperative Bank) plugin"""

    def get_parser(self, filename):
        f = open(filename, 'r', encoding=self.settings.get("charset", "UTF-8"))
        
        # skip line with columns names
        f.readline()
        
        parser = NewBParser(f)
        return parser
        
class NewBParser(CsvStatementParser):

    date_format = "%d/%m/%Y"

    #0 Numéro de compte;
    #1 Date;
    #2 Montant;
    #3 Devise;
    #4 Description;
    #5 Compte de la contrepartie;
    #6 Nom de la contrepartie;
    #7 Adresse de la contrepartie;
    #8 Communication;
    #9 Date valeur;
    #10 Solde du compte;
    #11 Devise;
    #12 Description personnelle;
    #13 Numéro d''extrait

    mappings = {
        'date': 1,
        'payee': 6,
        'memo': 8,
        'amount': 2
    }
        
    def __init__(self, filename):
        self.statement = Statement('NEECBEB2', None,'EUR')
        self.fin = filename
        csv.register_dialect('newbcsv', NewBCsv())
        
    def parse(self) -> Statement:
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        stmt = super(NewBParser, self).parse()
        recalculate_balance(stmt)
        return stmt

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        return csv.reader(self.fin, 'newbcsv')

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """
        self.statement.account_id =  line[0].replace(" ", "")
        #self.statement.account_to =  line[5].replace(" ", "")
        
        stmtline = super(NewBParser, self).parse_record(line)
        stmtline.id = generate_transaction_id(stmtline)
        stmtline.trntype = 'DEBIT' if stmtline.amount < 0 else 'CREDIT'                
        stmtline.bank_account_to = BankAccount(None, line[5].replace(" ", ""))

        return stmtline
