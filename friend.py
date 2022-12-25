import logging

logger = logging.getLogger('Friend')

class Friend:
    name = "HagOwl"
    its_me = False
    i_asked_to_meet = False
    asked_to_meet_me = False
    i_agree_to_meet = False

    def __init__(self, name, me):
        self.name = name
        self.its_me = me
    
    def update_status(self):
        #TODO: Save  meet requests and approvals to the server, and get meeting invites from server
        pass
    
    def ask_to_meet(self):
        if self.its_me:
            logger.warn("I can't ask myself to meet me!!!!")
        else:
            self.i_asked_to_meet = True
            logger.info("Asking {} to meet".format(self.name))
    
    def has_asked_to_meet_me(self):
        if self.its_me:
            logger.warn("I can't ask myself to meet me!!!!")
            return False
        else:
            return self.asked_to_meet_me
    
    def agree_to_meet_the_friend(self):
        if self.has_asked_to_meet_me():
            self.i_agree_to_meet = True
            logger.info("Agree to meet {}".format(self.name))
