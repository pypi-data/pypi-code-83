from decimal import *
getcontext().prec = 7


class Esser():
    def __init__(self, name, gewichtung):
        if type(gewichtung) not in (float, int):
            raise Exception('gewichtung must be float or int')
        if gewichtung < 0:
            # allow gewichtung 0 for placeholding
            raise Exception('gewichtung muss >= 0 sein')
        self.name = name
        self.gewichtung = Decimal(gewichtung)

    def __str__(self):
        return "%s (%.2f)" % (self.name, self.gewichtung)


class Einkauf():
    def __init__(self, betrag, esser, bezahler, datum=None, description=None, comment=None):
        if betrag <= 0:
            raise Exception('betrag <= 0')
        self.betrag = Decimal(betrag)
        if type(esser) not in (list, tuple):
            raise Exception('esser must be list or tuple')
        if type(bezahler) not in (str, list, tuple):
            raise Exception('bezahler must be str, list or tuple')
        self.esser = esser
        self.bezahler = bezahler
        self.datum = datum
        self.description = description
        self.comment = comment

    def len(self):
        """
        may return float or int
        """
        return sum([ e.gewichtung for e in self.esser if type(e) is Esser ]) + len([ e for e in self.esser if type(e) is not Esser ])

    def len_bezahler(self):
        """
        may return float or int
        """
        if type(self.bezahler) is str:
            return 1
        return sum([ e.gewichtung for e in self.bezahler if type(e) is Esser ]) + len([ e for e in self.bezahler if type(e) is not Esser ])


class Bezahlung():
    def __init__(self, bezahler, bezahlter, betrag, datum=None, description=None, comment=None):
        self.bezahler = bezahler
        self.bezahlter = bezahlter
        if betrag <= 0:
            raise Exception('betrag <= 0')
        self.betrag = Decimal(betrag)
        self.datum = datum
        self.description = description
        self.comment = comment


class Mahlzeit():
    def __init__(self):
        self.einkaeufe = list()
        self.bezahlungen = list()

        # for usage in context
        self.datum = None
        self.description = None
        self.comment = None

    def __call__(self, datum=None, description=None, comment=None):
        self.datum = datum
        self.description = description
        self.comment = comment
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.datum = None
        self.description = None
        self.comment = None

    def einkauf(self, betrag, esser, bezahler, datum=None, description=None, comment=None):
        self.einkaeufe.append(Einkauf(Decimal(betrag), esser, bezahler,
            datum=datum if datum else self.datum,
            description=description if description else self.description,
            comment=comment if comment else self.comment,
        ))

    def bezahlung(self, bezahler, bezahlter, betrag, datum=None, description=None, comment=None):
        self.bezahlungen.append(Bezahlung(bezahler, bezahlter, Decimal(betrag),
            datum=datum if datum else self.datum,
            description=description if description else self.description,
            comment=comment if comment else self.comment,
        ))

    def calc(self):
        vergessen = dict()
        ausgegeben = dict()
        ausgleich = dict()
        for e in self.einkaeufe:
            if type(e.bezahler) is str:
                ausgegeben[e.bezahler] = ausgegeben.get(e.bezahler, Decimal(0)) + e.betrag
            else:
                for bez in e.bezahler:
                    if type(bez) is Esser:
                        ausgegeben[bez.name] = ausgegeben.get(bez.name, Decimal(0)) + (e.betrag * Decimal(bez.gewichtung))/Decimal(e.len_bezahler())
                    else:
                        ausgegeben[bez] = ausgegeben.get(bez.name, Decimal(0)) + e.betrag/Decimal(e.len_bezahler())
            for p in e.esser:
                if type(p) is Esser:
                    vergessen[p.name] = Decimal(vergessen.get(p.name, Decimal(0))) + (e.betrag * Decimal(p.gewichtung))/Decimal(e.len())
                else:
                    vergessen[p] = Decimal(vergessen.get(p, Decimal(0))) + e.betrag/Decimal(e.len())
        for person in set(list(vergessen.keys()) + list(ausgegeben.keys())):
            ausgleich[person] = Decimal(ausgegeben.get(person, Decimal(0))) - Decimal(vergessen.get(person, Decimal(0)))
        for b in self.bezahlungen:
            ausgleich[b.bezahler] = ausgleich.get(b.bezahler, Decimal(0)) + b.betrag
            ausgleich[b.bezahlter] = ausgleich.get(b.bezahlter, Decimal(0)) - b.betrag

        # sanity check
        assert sum([ b for _, b in ausgleich.items() ]) < Decimal(0.01)

        return ausgleich

    def pretty(self):
        self.pprint()

    def pprint(self):
        for k, v in sorted(self.calc().items(), key=lambda x: x[1]):
            print("%10s %.2f" % (k, v))

    def reset(self):
        self.einkaeufe = list()
        self.bezahlungen = list()

    def journal(self):
        for eink in self.einkaeufe:
            if not eink.datum and not eink.description: continue
            if eink.comment:
                print(";", eink.comment)
            print(eink.datum, eink.description)
            if type(eink.bezahler) is str:
                print("\t%s\t\t%.2f" % (eink.bezahler, eink.betrag))
            else:
                for p in eink.bezahler:
                    if type(p) is Esser:
                        b = Decimal(eink.betrag * Decimal(p.gewichtung))/Decimal(eink.len_bezahler())
                        print("\t%s\t\t%.2f" % (p.name, b))
                    else:
                        b = eink.betrag/Decimal(eink.len_bezahler())
                        print("\t%s\t\t%.2f" % (p, b))
            for p in eink.esser:
                if type(p) is Esser:
                    b = Decimal(eink.betrag * Decimal(p.gewichtung))/Decimal(eink.len())
                    print("\t%s\t\t%.2f" % (p.name, -b))
                else:
                    b = eink.betrag/Decimal(eink.len())
                    print("\t%s\t\t%.2f" % (p, -b))
            print("\trounding")
            print()

        for bez in self.bezahlungen:
            if not bez.datum and not bez.description: continue
            if bez.comment:
                print(";", bez.comment)
            print(bez.datum, bez.description)
            print("\t%s\t\t%.2f" % (bez.bezahler, bez.betrag))
            print("\t%s" % (bez.bezahlter,))
            print()
