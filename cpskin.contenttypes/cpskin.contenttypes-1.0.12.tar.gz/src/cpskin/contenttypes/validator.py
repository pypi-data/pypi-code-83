# -*- coding: utf-8 -*-
from cpskin.locales import CPSkinMessageFactory as _
from imio.behavior.teleservices.behaviors.ts_procedure import ITsProcedure
from z3c.form import validator
from zope.interface import Invalid


class ProcedureValidator(validator.SimpleFieldValidator):

    def validate(self, value):
        form = self.widget.form
        e_guichet_value = form.widgets["e_guichet"].extract()
        if e_guichet_value and value:
            raise Invalid(_(u"Only one procedure field can be filled !"))


validator.WidgetValidatorDiscriminators(ProcedureValidator, field=ITsProcedure['procedures'])
