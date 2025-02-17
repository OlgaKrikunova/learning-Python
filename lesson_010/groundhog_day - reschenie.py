from random import choice, randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


class_random = (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError)


def one_day():
    carma_level = 0
    count = 0

    while carma_level < ENLIGHTENMENT_CARMA_LEVEL:
        rand_number = randint(1, 13)
        if rand_number != 13:

            carma_level += randint(1, 7)
        elif rand_number == 13:
            try:
                raise choice(class_random)("Что-то пошло не так!")
            except class_random as e:
                print(f" Возникла ошибка - {type(e).__name__} - {e}")
        count += 1
    print()
    print(f" Набрано кармы - {carma_level}, за {count} дней")


one_day()
