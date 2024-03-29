movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9,
        "John Wick": 9
    },
    "Морбиус": {}
}

def show():
    for name, rates in movies.items():
        print(f'\nMovies - {name}')
        if len(rates) == 0:
            print('Rating is not yet available.')
        else:
            print('Rate')
            for user, rate in rates.items():
                print(f'{user} : {rate}')


def add_movise(movie):
    if movie in movies.keys():
        print('This movie already exist!')
    else:
        movies.update({movies: dict()})


def add_rete(movie):
    if movie not in movies.keys():
        print("This movie doesn't exist")
    else:
        name = input('Enter your name:')
        rate = input('Enret rate:')
        if rate < 0 or rate > 10:
            print('Rate must be 1-10!')
        else:
            movies[movie].update({name: rate})
            print(f"A rating has been added for Interstellar: {name} rated it {rate}")


def rate_view():
    for movie, rate in movies.items():
        rates = []
        for i in rate.values():
            rates.append(i)
        if len(rates) == 0:
            print(f"Rating is not yet available for {movie}")
        else:
            print(sum(rates) / len(rates))


while True:
    show()
    command = int(input("\nEnter command(1 - add film, 2 - add rate, 3 - view rates, 0 - finish programm): "))

    if command == 0:
        print(f'Program is finish')
        break

    elif command == 1:
        movie = input('Enter movie:')
        add_movise(movie)
    elif command == 2:
        movie = input('Enter movie for add rate: ')
        add_movise(movie)
    elif command == 3:
        rate_view()
    else:
        print("Command doesn't exist!")