from flask import Blueprint, request
from models.movie import Movie
from extensions import db

movies = [
    {
        "name": "Thor: Ragnarok",
        "poster": "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_.jpg",
        "summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\\n of researchers, to find a new planet for humans.",
        "rating": 8.8,
        "trailer": "https://youtu.be/NgsQ8mVkN8w",
        "id": "109",
    },
    {
        "id": "99",
        "name": "Vikram",
        "poster": "https://m.media-amazon.com/images/M/MV5BMmJhYTYxMGEtNjQ5NS00MWZiLWEwN2ItYjJmMWE2YTU1YWYxXkEyXkFqcGdeQXVyMTEzNzg0Mjkx._V1_.jpg",
        "rating": 8.4,
        "summary": "Members of a black ops team must track and eliminate a gang of masked murderers.",
        "trailer": "https://www.youtube.com/embed/OKBMCL-frPU",
    },
    {
        "id": "100",
        "name": "RRR",
        "poster": "https://englishtribuneimages.blob.core.windows.net/gallary-content/2021/6/Desk/2021_6$largeimg_977224513.JPG",
        "rating": 8.8,
        "summary": "RRR is an upcoming Indian Telugu-language period action drama film directed by S. S. Rajamouli, and produced by D. V. V. Danayya of DVV Entertainments.",
        "trailer": "https://www.youtube.com/embed/f_vbAtFSEc0",
    },
    {
        "id": "101",
        "name": "Iron man 2",
        "poster": "https://m.media-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_FMjpg_UX1000_.jpg",
        "rating": 7,
        "summary": "With the world now aware that he is Iron Man, billionaire inventor Tony Stark (Robert Downey Jr.) faces pressure from all sides to share his technology with the military. He is reluctant to divulge the secrets of his armored suit, fearing the information will fall into the wrong hands. With Pepper Potts (Gwyneth Paltrow) and Rhodes (Don Cheadle) by his side, Tony must forge new alliances and confront a powerful new enemy.",
        "trailer": "https://www.youtube.com/embed/wKtcmiifycU",
    },
    {
        "id": "102",
        "name": "No Country for Old Men",
        "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
        "rating": 8.1,
        "summary": "A hunter's life takes a drastic turn when he discovers two million dollars while strolling through the aftermath of a drug deal. He is then pursued by a psychopathic killer who wants the money.",
        "trailer": "https://www.youtube.com/embed/38A__WT3-o0",
    },
    {
        "id": "103",
        "name": "Jai Bhim",
        "poster": "https://m.media-amazon.com/images/M/MV5BY2Y5ZWMwZDgtZDQxYy00Mjk0LThhY2YtMmU1MTRmMjVhMjRiXkEyXkFqcGdeQXVyMTI1NDEyNTM5._V1_FMjpg_UX1000_.jpg",
        "summary": "A tribal woman and a righteous lawyer battle in court to unravel the mystery around the disappearance of her husband, who was picked up the police on a false case",
        "rating": 8.8,
        "trailer": "https://www.youtube.com/embed/nnXpbTFrqXA",
    },
    {
        "id": "104",
        "name": "The Avengers",
        "rating": 8,
        "summary": "Marvel's The Avengers (classified under the name Marvel Avengers\n Assemble in the United Kingdom and Ireland), or simply The Avengers, is\n a 2012 American superhero film based on the Marvel Comics superhero team\n of the same name.",
        "poster": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/avengersendgame_lob_crd_05.jpg",
        "trailer": "https://www.youtube.com/embed/eOrNdBpGMv8",
    },
    {
        "id": "105",
        "name": "Interstellar",
        "poster": "https://m.media-amazon.com/images/I/A1JVqNMI7UL._SL1500_.jpg",
        "rating": 8.6,
        "summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\n of researchers, to find a new planet for humans.",
        "trailer": "https://www.youtube.com/embed/zSWdZVtXT7E",
    },
    {
        "id": "106",
        "name": "Baahubali",
        "poster": "https://flxt.tmsimg.com/assets/p11546593_p_v10_af.jpg",
        "rating": 8,
        "summary": "In the kingdom of Mahishmati, Shivudu falls in love with a young warrior woman. While trying to woo her, he learns about the conflict-ridden past of his family and his true legacy.",
        "trailer": "https://www.youtube.com/embed/sOEg_YZQsTI",
    },
    {
        "id": "107",
        "name": "Ratatouille",
        "poster": "https://resizing.flixster.com/gL_JpWcD7sNHNYSwI1ff069Yyug=/ems.ZW1zLXByZC1hc3NldHMvbW92aWVzLzc4ZmJhZjZiLTEzNWMtNDIwOC1hYzU1LTgwZjE3ZjQzNTdiNy5qcGc=",
        "rating": 8,
        "summary": "Remy, a rat, aspires to become a renowned French chef. However, he fails to realise that people despise rodents and will never enjoy a meal cooked by him.",
        "trailer": "https://www.youtube.com/embed/NgsQ8mVkN8w",
    },
    {
        "name": "PS2 🍊",
        "poster": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5MC00NGUyLWJiYWMtZDI3MTQ1MGU4OGY2XkEyXkFqcGdeQXVyNDExMjcyMzA@._V1_.jpg",
        "summary": "Ponniyin Selvan: I is an upcoming Indian Tamil-language epic period action film directed by Mani Ratnam, who co-wrote it with Elango Kumaravel and B. Jeyamohan",
        "rating": 8,
        "trailer": "https://www.youtube.com/embed/KsH2LA8pCjo",
        "id": "108",
    },
]

HTTP_NOT_FOUND = 404
HTTP_CREATED = 201
HTTP_ERROR = 500

movies_bp = Blueprint("movies_bp", __name__)


# @app.get("/movies")
# def get_all_movies():
#     # list of DICT -> JSON
#     return movies


@movies_bp.get("")
def get_all_movies():
    # List (Dict) -> JSON
    # Select * from movies
    movies = [movie.to_dict() for movie in Movie.query.all()]
    return movies


# BY ID


@movies_bp.get("/<id>")
def get_movie_by_id(id):
    data = Movie.query.get(id)
    # print(f"1st:{data}")
    if not data:
        return {"message": "Movie not found"}, HTTP_NOT_FOUND
    movie = data.to_dict()
    # print(movie)
    return movie


@movies_bp.delete("/<id>")
def delete_movie_by_id(id):
    data = Movie.query.get(id)

    if not data:
        return {"message": "Movie not found"}, HTTP_NOT_FOUND

    movie = data.to_dict()
    try:
        # Row lock
        db.session.delete(data)
        # raise Exception("Oh no")
        db.session.commit()
        # Row release
        return movie
    except Exception as err:
        db.session.rollback()
        return {"message": str(err)}, HTTP_ERROR


@movies_bp.post("/")
def create_movie():
    # List (Dict) -> JSON
    data = request.get_json()  # JSON -> Dict, List(Dict)
    # Movie(name=new_movie['name'], rating=new_movie['rating'])

    new_movie = Movie(**data)  # id
    try:
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.to_dict(), HTTP_CREATED
    except Exception as err:
        db.session.rollback()
        return {"message": str(err)}, HTTP_ERROR


@movies_bp.put("/<id>")
def update_movie(id):
    body = request.get_json()  # body

    print(id)

    try:
        updated = Movie.query.filter_by(id=id).update(body)

        if not updated:
            return {"message": "Movie not found"}, HTTP_NOT_FOUND

        db.session.commit()
        data = Movie.query.get(id)
        return data.to_dict()

    except Exception as err:
        db.session.rollback()
        return {"message": str(err)}, HTTP_ERROR


# @movies_bp.put("/<id>")
# def update_movie(id):
#     update_movie = request.get_json()  # body

#     for movie in movies:
#         if movie["id"] == id:
#             movie.update(update_movie)
#             return movie

#     return {"message": "Movie not found"}, HTTP_NOT_FOUND
