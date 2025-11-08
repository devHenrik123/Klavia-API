# Klavia-API
A python package for sending requests to the Rest API of the browser / typing game Klavia.

## Examples:

### Basic:
Loads access token from local .env file and gets wpm leaderboards.
```
if __name__ == "__main__":
    
    # Use .env file to store token securely:
    from pathlib import Path
    from dotenv import dotenv_values
    env_vars: Final[dict[str, str | None]] = dotenv_values(Path(__file__).parent.parent.resolve() / ".env")
    
    api_token: Final[str] = env_vars["api_token"]
    # KlaviaAPI(api_token).race_sessions_ongoing()
    # KlaviaAPI(api_token).leaderboards_races(TimePeriod.Season)
    # KlaviaAPI(api_token).leaderboards_points(TimePeriod.Season)
    # KlaviaAPI(api_token).leaderboards_accuracy(TimePeriod.Season)
    wpm_leaderboard: list[LeaderboardEntryWpm] = KlaviaAPI(api_token).leaderboards_wpm(TimePeriod.Season)
```
