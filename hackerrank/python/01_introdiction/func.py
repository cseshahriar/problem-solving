if __name__ == '__main__':
    def is_leap(year):
        leap = False
        # write your logic here
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

        return leap

    year = int(input())

    print(is_leap(year))