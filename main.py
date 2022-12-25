import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

from friend import Friend

ariel = Friend("Ariel", True)
elad = Friend("Elad", False)
itay = Friend("Itay", False)

def main():
    logger.info("Hello World!")
    itay.ask_to_meet()
    ariel.ask_to_meet()
    logger.info("Elad asked to meet me? {}".format(elad.has_asked_to_meet_me()))

if __name__ == "__main__":
    main()