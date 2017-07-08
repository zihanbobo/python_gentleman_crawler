import index.ActorDAO as ActorDAO
import index.IndexActor as indexActor
from index import ActorFinder

def saveMovieToDB(skipActors):
    if not skipActors:
        newActors  = ActorFinder.findActors()
        if len(newActors) > 0:
            print("find new actors:")
            print(newActors)
        else:
            print("no found new actor.")

    actors = ActorDAO.getAllActors()

    allMovies = []

    count = 600

    for actor in actors:
        count = count - 1
        if count < 0:
            break;

        print("begin to read: " + str(actor))
        newMovies = indexActor.saveActorToDB(url=actor["url"], actor=actor["name"], cache=False)
        #print("find new movies: " + str(newMovies))
        ActorDAO.updateLastReadTime(actor["name"])

    return allMovies

saveMovieToDB(True)