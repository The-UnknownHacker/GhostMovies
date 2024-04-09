# GhostMovies
GhostMovies is a mirror of [Movie-Web](https://github.com/movie-web/movie-web) with some changes...
The Official instance of GhostMovies can be found at [GhostMovies](https://movies.ghostai.me)

# Structure

This project works in 2 ways
1 - The Backend is the actual GhostMovies service serving the ui frontend
2 - The frontend or login system. This system prevents abuse of the project
 - To get this project setup you will have to run the backend as shown below then run the frontend using the frontend instruction below

**I *do not* endorse piracy of any kind I simply enjoy programming and large user counts.**


## Links And Resources
| Service        | Link                                               | Source Code                                              |
|----------------|----------------------------------------------------|----------------------------------------------------------|
| Movie-Web Docs | [movie-web-docs](https://movie-web.github.io/docs) | [Source Code](https://github.com/movie-web/docs)         |
| Extension      | [movie-web plugin](https://shorturl.at/iqzES)      | [Source Code](https://github.com/movie-web/extension)    |
| Proxy          | [sudo-proxy](https://sudo-proxy1.GhostMovies.lol)    | [Source Code](https://gitlab.com/GhostMovies/simple-proxy) |
| Backend        | [sudo-backend](https://backend.GhostMovies.lol)      | [Source Code](https://github.com/movie-web/backend)      |
| Frontend       | [GhostMovies](https://sudo-flix.lol)                 | [Source Code](https://github.com/sussy-code/smov)  |

**I provide these if you are not able to host yourself, though I do encourage hosting the frontend.**


## Referrers
- [Priacy Subreddit Megathread](https://www.reddit.com/r/Piracy/s/iymSloEpXn)
- [Toon's Instances](https://erynith.github.io/movie-web-instances)
- [Movie-Web Docs](https://movie-web.github.io/docs/instances)
- [Movie-Web Discord](https://movie-web.github.io/links/discord)
- Search Engines: DuckDuckGo, Bing, Google
- Rentry.co? (This ones a mystery)


## Running Locally
Type the following commands into your terminal / command line to run The GhostMovies Backend Locally
```bash
git clone https://github.com/The-UnknownHacker/GhostMovies/
cd GhostMovies
git pull
pnpm install
pnpm run dev
```
Then you can visit the local instance [here](http://localhost:5173) or, at local host on port 5173, or at 127.0.0.1:5173
Or 
You can host the frontend with the login system

## Hosting the Frontend
Type the following commands into your terminal / command line to run The GhostMovies Frontend Locally
**You need to already be hosting the backend for this to work Otherwise it won't work**
```bash
cd GhostMovies
git pull
pip install Flask Flask-Login Werkzeug
python main.py or python3 main.py
```
Then you can visit the final instance [here](http://localhost:5000) or, at local host on port 5000, or at 127.0.0.1:5000





