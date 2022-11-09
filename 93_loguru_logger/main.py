from loguru import logger

logger.add("logger.log", )

logger.error("This is an error")
logger.info("This is an info message")


def test():
    logger.info("This is an info message from test()")


class Test:
    def __init__(self):
        logger.info("This is an info message from Test.__init__()")

    def test(self):
        logger.info("This is an info message from Test.test()")


test()

logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod


def func(a, b):
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


nested(0)
