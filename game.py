from Models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    difficulty: int = int(input('Enter the desired difficulty level [1, 2, 3 ou 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('Report the result for the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'You have {points} point(s).')

    keep: int = int(input('Do you want to continue in the game? [1 - Yes, 2 - No] '))

    if keep == 1:
        play(points)
    else:
        print(f'You ended up with {points} point(s).')
        print(f'Until next time!')


if __name__ == '__main__':
    main()