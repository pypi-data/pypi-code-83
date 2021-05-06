import os

from otree.api import BaseConstants, BaseGroup, BasePlayer, BaseSubsession

author = "Philipp Külpmann"

doc = """
App to gather payment data from subjects
"""

output_col_names = ["full_name", "iban", "bic"]


class Constants(BaseConstants):
    name_in_url = "vceepayment"
    players_per_group = None
    num_rounds = 1
    default_waiting_for_others = True


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        with open("payment_info.csv", "r") as f:
            return {"file_path": f.read()}

    def creating_session(self):
        try:
            encrypt = self.session.config["encrypt_payment_file"]
        except KeyError:
            self.session.config["encrypt_payment_file"] = False
            encrypt = False
        if not os.path.isfile("public_shared.pem") and encrypt:
            raise FileNotFoundError(
                "Encryption enabled but no public key found! Either upload the public key or disable encryption."
            )

        for player in self.get_players():
            player.participant.vars["temp_values"] = {
                item: "" for item in output_col_names
            }


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
