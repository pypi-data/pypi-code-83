import json
from datetime import datetime

from vaccineAvailabilityNotifier.client.actionsImpl import ActionsImpl
from vaccineAvailabilityNotifier.email.email_sender import send_email


class ProcessJob:
    __action_processor = ActionsImpl()

    def __init__(self, sender_email_id, sender_email_password, pincodes, receiver_email, include_45):
        self.sender_email_id = sender_email_id
        self.sender_email_password = sender_email_password
        self.pincodes = pincodes
        self.receiver_email = receiver_email
        self.include_45 = include_45

    def process(self):
        print('email : ' + self.sender_email_id)
        print(self.pincodes)
        print("\n\n\n")
        # print(datetime.today().strftime('%d-%m-%Y'))
        responses = []
        for pincode in self.pincodes:
            responses.append(
                self.__action_processor.get({'pincode': pincode, 'date': datetime.today().strftime('%d-%m-%Y')}))

        print(len(responses))
        print(responses.__str__())

        for response in responses:
            res = json.loads(response.content.decode('utf-8'))

            if response.status_code == 200:

                for center in res['centers']:
                    # print(center)
                    # print(center["sessions"])
                    if (self.include_45):
                        available_centers = list(
                            filter(lambda x: x.get("available_capacity") > 0, center["sessions"]))
                    else:
                        available_centers = list(
                            filter(lambda x: x.get("available_capacity") > 0 and x.get("min_age_limit") == 18,
                                   center["sessions"]))

                    print(available_centers)

                    if len(available_centers) > 0:

                        send_email(json.dumps(center, indent=3), sender_email_id=self.sender_email_id,
                                   sender_email_password=self.sender_email_password,
                                   receiver_email_id=self.receiver_email)
                    else:
                        print('slot is not available')

                # print(res)
            else:
                print(res)
                exit()

        print(" run completed !!")
