from __future__ import unicode_literals
from __future__ import print_function
import got
import sys
import time
from io import StringIO
from colorama import init, deinit


def digits(number):
    return len(str(number))


def main():
    sys.stdout = StringIO()
    got.reset_game()

    ronde = 1

    while not got.is_game_over():

        sys.stdout = StringIO()
        print("------------------" + digits(ronde) * "-" + "------------")
        print("------      Ronde " + str(ronde) + "      ------")
        print("------------------" + digits(ronde) * "-" + "------------")

        got.toon_wereld_informatie()

        for fase in range(1, 3):
            if not got.is_game_over():
                is_ai = fase == 2
                actie = got.bepaal_ronde_actie(is_ai)
                if actie != '':
                    eval("got.{}(is_ai)".format(actie))

        if not got.is_game_over():
            got.verplaats()

        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__
        init()
        print(output)
        deinit()

        print("Verder in ", end='')
        sys.stdout.flush()
        for t in range(60, 0, -2):
            time.sleep(0.2)
            if t % 10 == 0:
                print(str(t // 10), end='')
            else:
                print(".", end='')

            sys.stdout.flush()

        print('')

        ronde += 1

    got.toon_game_over()


if __name__ == "__main__":
    main()
