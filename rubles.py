def result(money, length_money, money2):
    def dozens():
        match money2[0]:
            case '9':
                print('Девяносто ', end='')
            case '8':
                print('Восемьдесят ', end='')
            case '7':
                print('Семьдесят ', end='')
            case '6':
                print('Шестьдесят ', end='')
            case '5':
                print('Пятьдесят ', end='')
            case '4':
                print('Сорок ', end='')
            case '3':
                print('Тридцать ', end='')
            case '2':
                print('Двадцать ', end='')
            case _:
                match money2[1]:
                    case '9':
                        if length_money == 5:
                            print('Девятнадцать тысяч', end='')
                        else:
                            print('Девятнадцать рублей', end='')
                    case '8':
                        if length_money == 5:
                            print('Восемнадцать тысяч', end='')
                        else:
                            print('Восемнадцать рублей', end='')
                    case '7':
                        if length_money == 5:
                            print('Семнадцать тысяч', end='')
                        else:
                            print('Семнадцать рублей', end='')
                    case '6':
                        if length_money == 5:
                            print('Шестнадцать тысяч', end='')
                        else:
                            print('Шестнадцать рублей')
                    case '5':
                        if length_money == 5:
                            print('Пятнадцать тысяч', end='')
                        else:
                            print('Пятнадцать рублей')
                    case '4':
                        if length_money == 5:
                            print('Четырнадцать тысяч', end='')
                        else:
                            print('Четырнадцать рублей')
                    case '3':
                        if length_money == 5:
                            print('Тринадцать тысяч', end='')
                        else:
                            print('Тринадцать рублей')
                    case '2':
                        if length_money == 5:
                            print('Двенадцать тысяч', end='')
                        else:
                            print('Двенадцать рублей')
                    case '1':
                        if length_money == 5:
                            print('Одиннадцать тысяч', end='')
                        else:
                            print('Одиннадцать рублей')
                    case _:
                        if length_money == 5:
                            print('Десять тысяч', end='')
                        else:
                            print('Десять рублей')

    def dozens2():
        match money2[-2]:
            case '9':
                print('девяносто ', end='')
            case '8':
                print('восемьдесят ', end='')
            case '7':
                print('семьдесят ', end='')
            case '6':
                print('шестьдесят ', end='')
            case '5':
                print('пятьдесят ', end='')
            case '4':
                print('сорок ', end='')
            case '3':
                print('тридцать ', end='')
            case '2':
                print('двадцать ', end='')
            case '1':
                match money2[-1]:
                    case '9':
                        print('девятнадцать рублей')
                    case '8':
                        print('восемнадцать рублей')
                    case '7':
                        print('семнадцать рублей')
                    case '6':
                        print('шестнадцать рублей')
                    case '5':
                        print('пятнадцать рублей')
                    case '4':
                        print('четырнадцать рублей')
                    case '3':
                        print('тринадцать рублей')
                    case '2':
                        print('двенадцать рублей')
                    case '1':
                        print('одиннадцать рублей')
                    case _:
                        print('десять рублей')

    def units():
        match money2[0]:
            case '9':
                if length_money == 4:
                    print('Девять тысяч ', end='')
                else:
                    print('Девять рублей', end='')
            case '8':
                if length_money == 4:
                    print('Восемь тысяч ', end='')
                else:
                    print('Восемь рублей', end='')
            case '7':
                if length_money == 4:
                    print('Семь тысяч ', end='')
                else:
                    print('Семь рублей')
            case '6':
                if length_money == 4:
                    print('Шесть тысяч ', end='')
                else:
                    print('Шесть рублей')
            case '5':
                if length_money == 4:
                    print('Пять тысяч ', end='')
                else:
                    print('Пять рублей')
            case '4':
                if length_money == 4:
                    print('Четыре тысячи ', end='')
                else:
                    print('Четыре рубля')
            case '3':
                if length_money == 4:
                    print('Три тысячи ', end='')
                else:
                    print('Три рубля')
            case '2':
                if length_money == 4:
                    print('Две тысячи ', end='')
                else:
                    print('Два рубля')
            case _:
                if length_money == 4:
                    print('Одна тысяча ', end='')
                else:
                    print('Один рубль')

    def units3():
        match money2[-1]:
            case '9':
                if money2[-2] != '1':
                    print('девять рублей')
            case '8':
                if money2[-2] != '1':
                    print('восемь рублей')
            case '7':
                if money2[-2] != '1':
                    print('семь рублей')
            case '6':
                if money2[-2] != '1':
                    print('шесть рублей')
            case '5':
                if money2[-2] != '1':
                    print('пять рублей')
            case '4':
                if money2[-2] != '1':
                    print('четыре рубля')
            case '3':
                if money2[-2] != '1':
                    print('три рубля')
            case '2':
                if money2[-2] != '1':
                    print('два рубля')
            case '1':
                if money2[-2] != '1':
                    print('один рубль')
            case '0':
                if money2[-2] != '1':
                    print('рублей')

    def hundreds():
        match money2[0]:
            case '9':
                print('Девятьсот ', end='')
            case '8':
                print('Восемьсот ', end='')
            case '7':
                print('Семьсот ', end='')
            case '6':
                print('Шестьсот ', end='')
            case '5':
                print('Пятьсот ', end='')
            case '4':
                print('Четыреста ', end='')
            case '3':
                print('Триста ', end='')
            case '2':
                print('Двести ', end='')
            case _:
                print('Сто ', end='')

    def hundreds2():
        match money2[-3]:
            case '9':
                print('девятьсот ', end='')
            case '8':
                print('восемьсот ', end='')
            case '7':
                print('семьсот ', end='')
            case '6':
                print('шестьсот ', end='')
            case '5':
                print('пятьсот ', end='')
            case '4':
                print('четыреста ', end='')
            case '3':
                print('триста ', end='')
            case '2':
                print('двести ', end='')
            case _:
                print('сто ', end='')

    def units2():
        match money2[1]:
            case '9':
                if money2[0] != '1':
                    print('девять тысяч ', end='')
            case '8':
                if money2[0] != '1':
                    print('восемь тысяч ', end='')
            case '7':
                if money2[0] != '1':
                    print('семь тысяч ', end='')
            case '6':
                if money2[0] != '1':
                    print('шесть тысяч ', end='')
            case '5':
                if money2[0] != '1':
                    print('пять тысяч ', end='')
            case '4':
                if money2[0] != '1':
                    print('четыре тысячи ', end='')
            case '3':
                if money2[0] != '1':
                    print('три тысячи ', end='')
            case '2':
                if money2[0] != '1':
                    print('две тысячи', end='')
            case '1':
                if money2[0] != '1':
                    print('одна тысяча', end='')
            case _:
                print(' ')

    match length_money:
        case 6:
            if money == 100000:
                print('Сто тысяч рублей')
        case 5:
            if int(money) >= 1:
                dozens(), units2(), hundreds2(), dozens2(), units3()
        case 4:
            if int(money) >= 1:
                units(), hundreds2(), dozens2(), units3()
        case 3:
            if int(money) >= 1:
                hundreds(), dozens2(), units3()
        case 2:
            if int(money) >= 1:
                dozens(), units3()
        case 1:
            if int(money) >= 1:
                units()
