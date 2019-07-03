"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day27_logging.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

import logging


log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()
logger.setLevel("DEBUG")
logger.debug("This is a custom debug message.")
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")
logger.error("This is a custom error message.")
logger.critical("This is a custom critical message.")

def quadratic_formula(a: float, b: float, c: float) -> (float, float):
    """
    Solve for x in the quadratic formula.
        ax^2 + bx + c = 0
    :param a: float
    :param b: float
    :param c: float
    :return: Solve for x, Return the positive and negative roots as float in a tuple
    """
    logger.info(f"Quadratic Formula Solver: {a}x^2 + {b}x + {c} = 0")

    # Calculate the discriminant
    logger.debug(f"Calculate the discriminant: {b}^2 - 4*{a}*{c}")
    discrim = (b ** 2) - (4 * a * c)
    logger.debug(f"Discriminant: {discrim}")

    # Calculate the positive and negative roots
    logger.debug(f"Calculate the pos/neg roots: (-{b} +/- sqrt({discrim})) / (2*{a})")
    try:
        pos_root = (-b + (discrim ** 0.5)) / (2 * a)
        neg_root = (-b - (discrim ** 0.5)) / (2 * a)
        logger.debug(f"Positive Root: {pos_root}, Negative Root: {neg_root}")
        return pos_root, neg_root
    except ZeroDivisionError as err:
        logger.error(f"{a} cannot be equal to zero.\n{err}")
        raise
    except TypeError as err:
        logger.error(f"Invalid type.\n{err}")
        raise
    except ValueError as err:
        logger.error(f"Invalid value.\n{err}")
        raise
    finally:
        logger.debug("Function Complete")


roots = quadratic_formula(3, 4, 5)
print(roots)