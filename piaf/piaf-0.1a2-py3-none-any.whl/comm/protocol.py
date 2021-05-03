# coding: utf-8
"""
This module defines various object to play with FIPA protocols.
"""
import piaf.comm as comm


class RequestInteractionMsgFactory:
    @staticmethod
    def sendRequestMessage():
        pass

    @staticmethod
    def sendRefuseMessage(msg: "comm.ACLMessage"):
        pass

    @staticmethod
    def sendAgreeMessage(msg: "comm.ACLMessage"):
        pass

    @staticmethod
    def sendFailureMessage(msg: "comm.ACLMessage"):
        pass

    @staticmethod
    def sendInformDoneMessage(msg: "comm.ACLMessage"):
        pass

    @staticmethod
    def sendInformResultMessage(msg: "comm.ACLMessage"):
        pass

    @staticmethod
    def sendCancelMessage(msg: "comm.ACLMessage"):
        pass
