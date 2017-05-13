import index.ActorDAO as ActorDAO
import index.IndexActor as indexActor

def saveMovieToDB():
    actors = ActorDAO.getAllActors()

    allMovies = []

    count = 200

    for actor in actors:
        count = count - 1
        if count < 0:
            break;

        print("begin to read: " + str(actor))
        newMovies = indexActor.saveActorToDB(url=actor["url"], actor=actor["name"], cache=False)
        print("find new movies: " + str(newMovies))
        ActorDAO.updateLastReadTime(actor["name"])

    return allMovies

saveMovieToDB()