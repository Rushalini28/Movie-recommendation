
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.7},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4},
    {"title": "John Wick", "genre": "Action", "rating": 7.4},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8},
    {"title": "Titanic", "genre": "Romance", "rating": 7.9},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0},
    {"title": "The Conjuring", "genre": "Horror", "rating": 7.5},
    {"title": "A Quiet Place", "genre": "Horror", "rating": 7.5},
    {"title": "Get Out", "genre": "Horror", "rating": 7.8},
    {"title": "3 Idiots", "genre": "Comedy", "rating": 8.4},
    {"title": "Home Alone", "genre": "Comedy", "rating": 7.7},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7},
    {"title": "Dangal", "genre": "Drama", "rating": 8.3},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
]


def show_genres():
    genres = sorted(set(movie["genre"] for movie in movies))

    print("\nAvailable Genres:")
    for number, genre in enumerate(genres, start=1):
        print(f"{number}. {genre}")

    return genres


def recommend_movies():
    genres = show_genres()

    choice = input("\nEnter a genre: ").strip().lower()

    matching_movies = [
        movie for movie in movies
        if movie["genre"].lower() == choice
    ]

    if not matching_movies:
        print("\nSorry, genre not found. Please try again.")
        return

    matching_movies.sort(
        key=lambda movie: movie["rating"],
        reverse=True
    )

    print(f"\n🎬 Recommended {choice.title()} Movies")
    print("-" * 40)

    for number, movie in enumerate(matching_movies, start=1):
        print(
            f"{number}. {movie['title']} "
            f"| Rating: {movie['rating']}/10"
        )


def search_movie():
    name = input("\nEnter a movie name: ").strip().lower()

    results = [
        movie for movie in movies
        if name in movie["title"].lower()
    ]

    if results:
        print("\nMovie Details:")
        for movie in results:
            print(f"Title: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            print(f"Rating: {movie['rating']}/10")
            print("-" * 25)
    else:
        print("\nMovie not found.")


def main():
    while True:
        print("\n" + "=" * 35)
        print("     MOVIE RECOMMENDATION APP")
        print("=" * 35)
        print("1. Get movie recommendations")
        print("2. Search for a movie")
        print("3. View available genres")
        print("4. Exit")

        option = input("\nEnter your choice (1-4): ").strip()

        if option == "1":
            recommend_movies()
        elif option == "2":
            search_movie()
        elif option == "3":
            show_genres()
        elif option == "4":
            print("\nThanks for using Movie Recommendation App!")
            break
        else:
            print("\nInvalid choice. Enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
