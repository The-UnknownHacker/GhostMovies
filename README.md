# GhostMovies
GhostMovies is a mirror of [Movie-Web](https://github.com/movie-web/movie-web) with some changes...

**I *do not* endorse piracy of any kind I simply enjoy programming and large user counts.**


## Links And Resources
| Service        | Link                                               | Source Code                                              |
|----------------|----------------------------------------------------|----------------------------------------------------------|
| Movie-Web Docs | [movie-web-docs](https://movie-web.github.io/docs) | [Source Code](https://github.com/movie-web/docs)         |
| Extension      | [movie-web plugin](https://shorturl.at/iqzES)      | [Source Code](https://github.com/movie-web/extension)    |
| Proxy          | [sudo-proxy](https://sudo-proxy1.GhostMovies.lol)    | [Source Code](https://gitlab.com/GhostMovies/simple-proxy) |
| Backend        | [sudo-backend](https://backend.GhostMovies.lol)      | [Source Code](https://github.com/movie-web/backend)      |
| Frontend       | [GhostMovies](https://GhostMovies.lol)                 | [Source Code](https://github.com/sussy-code/smov)  |

**I provide these if you are not able to host yourself, though I do encourage hosting the frontend.**


## Referrers
- [Priacy Subreddit Megathread](https://www.reddit.com/r/Piracy/s/iymSloEpXn)
- [Toon's Instances](https://erynith.github.io/movie-web-instances)
- [Movie-Web Docs](https://movie-web.github.io/docs/instances)
- [Movie-Web Discord](https://movie-web.github.io/links/discord)
- Search Engines: DuckDuckGo, Bing, Google
- Rentry.co? (This ones a mystery)


## Running Locally
Type the following commands into your terminal / command line to run GhostMovies locally
```bash
git clone https://github.com/sussy-code/smov.git
cd GhostMovies
git pull
pnpm install
pnpm run dev
```
Then you can visit the local instance [here](http://localhost:5173) or, at local host on port 5173.


## Updating Instances

### GhostMovies
To update a GhostMovies instance you can type the below commands into a terminal at the root of your project.
```bash
git remote add upstream https://github.com/sussy-code/smov.git
git fetch GhostMovies  # Grab the contents of the new remote source
git checkout <YOUR_MAIN_BRANCH>  # Most likely this would be `origin/main`
git merge upstream/main
# * Fix any conflicts present during merge *
git add .  # Add all changes made during merge and conflict fixing
git commit -m "Update GhostMovies instance (merge upstream/main)"
git push  # Push to YOUR repository
```

### movie-web
To update a movie-web instance you can type the below commands into a terminal at the root of your project.  
movie-web has two branches `master` and `dev` GhostMovies always merges the dev branch to get the most recent updates, master is just a stable branch.

**Note:** To change the target branch for your merge simply replace `master` with `dev` or any other existing branch on the movie-web [repository](https://github.com/movie-web/movie-web).

```bash
git remote add movie-web https://github.com/movie-web/movie-web.git
git fetch movie-web  # Grab the contents of the new remote source
git checkout <YOUR_MAIN_BRANCH>  # Most likely this would be `origin/main`
git merge movie-web/master
# * Fix any conflicts present during merge *
git add .  # Add all changes made during merge and conflict fixing
git commit -m "Update movie-web instance (merge movie-web/master)"
git push  # Push to YOUR repository
```


## Contact Me
**Discord:** *.baddeveloper*  
**Email:** *[dev@GhostMovies.lol](mailto:dev@GhostMovies.lol)*
