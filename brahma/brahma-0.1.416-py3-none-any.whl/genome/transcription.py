"""Transcription genetic material/process is responsible for building the protein.
Here we model the action of decision making as the bot able to transcrible protein.
All the dna material in the bot is the genetic material required to regulate and transcribe
three different protein types:
1. An enzyme whose presence prescribes a 'ACTIVE' state
2. An enzyme whose presence prescribes a 'WAIT' state

This class/module is also considered 'genetic material', but it; sole responsibilty is to transcribe the already
exisiting genetic material. The genetic state of the gene(s) modelled here is/are always on (1/True).

gene state->genome->chromosome->expression vector-> [environmental regulation] -> transcription

[environmental regulation] will simply promote/suppress the expression vector rather than work on the transcrition
state

"""
import random, logging


class Transcription(object):
    """This class models the genetic material required to transcribe the 'bot's' genetic material.
    It reads in chromosomal expression levels and decides whether

    Arguments:
        object {[type]} -- [description]


    """

    def __init__(self):

        self.transcription_state = None
        self.transcription_state_recorder = {}
        #self.transcription_threshold = random.random()
        #self.transcription_threshold = 0.002
        self.transcription_threshold = random.random()
        #v2. update - Apr 16
        self.transcription_threshold_exit = random.random()

    def __str__(self):
        return ("Activation Level: {0}".format(self.transcription_threshold))

    def get_structure(self):
        transcription_str = {}
        transcription_str['state'] = self.transcription_state
        transcription_str['threshold'] = self.transcription_threshold_exit

    def transcribe(self, expression_data):
        """Transcribe DNA into protein

        Arguments:
            expression_data {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        #print ("state {0}".format(self.transcription_state))
        #check risk transcription first

        #risk
        risk_expression_str = expression_data['risk_expression_data']

        risk_expression_vec = []

        for chromTag, expression in risk_expression_str.items():
            risk_expression_vec.append(expression)

            #print (expression)
            if expression == 1:
                protein_transcribe = False
                self.transcription_state = False
                #print ("Exiting: {0} {1}".format(expression_data['pl'], expression_data['name']))
                logger.critical("Exiting from risk: {0} {1}".format(expression_data['pl'], expression_data['name']))
                return protein_transcribe



        #not risk
        expression_str = expression_data['expression_data']

        expression_vec = []

        for chromTag, expression in expression_str.items():
            expression_vec.append(expression)

        if TRANSCRIPTION_DEBUG:
            print ("Expression vector sent: ")
            print (expression_vec)

        protein_transcribe = self.map_expression_vector(expression_vec)
        #protein_transcribe = True

        if protein_transcribe == True:

            if TRANSCRIPTION_DEBUG:
                print ("Transcribing")
            self.transcription_state = True
            return protein_transcribe
        '''
        if protein_transcribe == False:

            if self.transcription_state == True:
                logger.critical("Exiting from threshold, not risk: {0}".format(expression_data['pl']))
            if TRANSCRIPTION_DEBUG:
                print ("Not Transcribing")
            self.transcription_state = False
            #print (expression_data['pl'])

            return protein_transcribe
        '''

    def map_expression_vector(self, e_data=None):
        """Map expression vector. State function on expression vector to determine
        transcription state.

        Keyword Arguments:
            e_vector {[type]} -- [description] (default: {None})
        """
        express_sum = 0
        number_express = len(e_data)

        for expression in e_data:
            express_sum = express_sum + expression

        transcription_activity = express_sum/number_express
        #see if trade triggered
        if transcription_activity > self.transcription_threshold:

            if TRANSCRIPTION_DEBUG:
                print ("activity: {0} threshold: {1}".format(transcription_activity, self.transcription_threshold))
            return True


        '''
        #if not already in trade
        if self.transcription_state == False:

            if transcription_activity > self.transcription_threshold:

                if TRANSCRIPTION_DEBUG:
                    print ("activity: {0} threshold: {1}".format(transcription_activity, self.transcription_threshold))
                return True


            else:

                return False
        '''
        '''
        if self.transcription_state == True:
            #stay in trade
            print (":SFSFS")
            return True
        '''



        '''
        #if already in trade
        if self.transcription_state == True:

            if transcription_activity < self.transcription_threshold_exit:
                if TRANSCRIPTION_DEBUG:
                    print ("activity: {0} threshold: {1}".format(transcription_activity, self.transcription_threshold_exit))
                #return False






        else:
            if TRANSCRIPTION_DEBUG:
                print ("activity: {0} threshold: {1}".format(transcription_activity, self.transcription_threshold))
            #return False

        '''



    def mutate(self):
        self.transcription_threshold = random.random()
        self.transcription_threshold_exit = random.random()


if __name__=="__main__":
    trans = Transcription()
    data = { 'expression_data':[0.3,0,0.65,0] }
    trans.transcribe(data)
