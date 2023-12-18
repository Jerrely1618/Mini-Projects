from loguru import logger


def example1():
    logger.debug("Log the log.")
    logger.info("Irrelevant Info here.")
    logger.success("Yeah! You won!")

@logger.catch
def example2(x = 3, y = 'a'):
    return x + y

if __name__ == "__main__":
    logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
    # example1()    
    # example2()
    
    








