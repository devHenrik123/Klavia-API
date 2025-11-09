# Klavia-API
A python package for sending requests to the Rest API of the browser / typing game Klavia.


## Installation
1. Install the module by adding it to your requirements.txt file like so:
```git+https://github.com/devHenrik123/Klavia-API.git@main```
2. Install dependencies like so: ```pip install -r requirements.txt```

## Basic Example:
Loads access token from local .env file and gets wpm leaderboards for the entire season.
```
if __name__ == "__main__":
    
    # Use .env file to store token securely:
    from pathlib import Path
    from dotenv import dotenv_values
    env_vars: Final[dict[str, str | None]] = dotenv_values(Path(__file__).parent.parent.resolve() / ".env")
    
    api_token: Final[str] = env_vars["api_token"]
    api: KlaviaAPI = KlaviaAPI(api_token)
    wpm_leaderboard: list[LeaderboardEntryWpm] = api.leaderboards_wpm(TimePeriod.Season)
```
