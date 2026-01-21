from lactec.intranet import logger
from zope.interface.interfaces import ObjectEvent


def checkallevents(obj, event: ObjectEvent):

    logger.info(event)
