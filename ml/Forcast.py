from index import MovieDAO
from index import SysConst
from ml import BayesTrainingFromDB as bayes


def forcastToDB():
    localBayes = bayes.BayesTrainingFromDB("local")
    vrBayes = bayes.BayesTrainingFromDB("vr")

    movies = MovieDAO.getMoviesByCondition("local is null")
    conn = SysConst.getConnect()

    for movie in movies:
        local = localBayes.classify(movie["title"])
        vr = vrBayes.classify(movie["title"])

        if local == "pos" and vr == "pos":
            movie["vr_forcast"] = 1
        else:
            movie["vr_forcast"] = 0

        MovieDAO.updateMovieFile(conn, movie)

    conn.commit()
    conn.close()


def forcastToNumbers():
    localBayes = bayes.BayesTrainingFromDB("local")
    vrBayes = bayes.BayesTrainingFromDB("vr")

    movies = MovieDAO.getMoviesByCondition("local is null")

    for movie in movies:
        # token = movie["av_number"] + movie["actor"] + movie["title"]
        token = movie["av_number"] + movie["title"]
        local = localBayes.probable(token)
        vr = vrBayes.probable(token)

        movie["vr_forcast"] = local + vr

    movies = sorted(movies, key=lambda d: d['vr_forcast'], reverse=True)

    numbers = []
    for i in range(0, 80):
        print(movies[i])
        numbers.append(movies[i]["av_number"])

    return numbers;


global allForcastMovies
allForcastMovies = False

def forcastMovies(start, limit):
    global allForcastMovies

    if not allForcastMovies:
        print("do forcast")
        localBayes = bayes.BayesTrainingFromDB("local")
        vrBayes = bayes.BayesTrainingFromDB("vr")
        skipBayes = bayes.BayesTrainingFromDB("skip")
        trashBayes = bayes.BayesTrainingFromDB("trash")

        movies = MovieDAO.getMoviesByCondition("local = 0 and trash = 0 and skip = 0")

        for movie in movies:
            token = movie["av_number"] + movie["actor"] + movie["title"]
            # token = movie["av_number"] + movie["title"]
            local = localBayes.probable(token)
            vr = vrBayes.probable(token)
            skip = skipBayes.probable(token)
            trash = trashBayes.probable(token)

            #movie["vr_forcast"] = local + vr
            movie["vr_forcast"] = vr - skip * 0.4 - trash * 0.01 + local * 0.3

        allForcastMovies = sorted(movies, key=lambda d: d['vr_forcast'], reverse=True)

    movies = allForcastMovies[start:(start+limit)]

    '''
    numbers = []
    for i in range(0, 100):
        #print(movies[i])
        numbers.append(movies[i])
    '''
    return movies;

def countForcastMovies():
    return len(allForcastMovies)
