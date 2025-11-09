from datetime import datetime
from enum import StrEnum
from typing import Final

from requests import Response, get

from data_models import RaceSession, LeaderboardEntryRaces, LeaderboardEntryPoints, LeaderboardEntryAccuracy, \
    LeaderboardEntryWpm

"""
/api/v1/race_sessions/ongoing

Leaderboards endpoints (Races/Points/Accuracy/WPM)

/api/v1/leaderboards/races
/api/v1/leaderboards/points
/api/v1/leaderboards/accuracy
/api/v1/leaderboards/wpm

Parameters
tp: The time period. Accepted values are season or 24h
"""


class TimePeriod(StrEnum):
    Season = "season",
    TP_24h = "24h"


class KlaviaAPI:
    # ========================================================================
    # Constants / URLs:

    # General:
    Klavia_Url: Final[str] = "https://klavia.io"
    API_v1: Final[str] = Klavia_Url + "/api/v1"

    # Sessions:
    RaceSessions: Final[str] = API_v1 + "/race_sessions"
    RaceSessions_Ongoing: Final[str] = RaceSessions + "/ongoing"

    # Leaderboards:
    Leaderboards: Final[str] = API_v1 + "/leaderboards"
    Leaderboards_Races: Final[str] = Leaderboards + "/races"
    Leaderboards_Points: Final[str] = Leaderboards + "/points"
    Leaderboards_Accuracy: Final[str] = Leaderboards + "/accuracy"
    Leaderboards_WPM: Final[str] = Leaderboards + "/wpm"

    # ========================================================================

    def __init__(self, access_token: str) -> None:
        self._access_token: Final[str] = access_token

    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._access_token}"
        }

    def race_sessions_ongoing(self) -> list[RaceSession]:
        resp: Response = get(
            url=KlaviaAPI.RaceSessions_Ongoing,
            headers=self.headers()
        )
        race_sessions: list[RaceSession] = [
            RaceSession(
                racer_id=session["racerId"],
                user_name=session["userName"],
                team=session["team"],
                started_at=datetime.fromisoformat(session["startedAt"]),
                last_race_at=datetime.fromisoformat(session["lastRaceAt"]),
                races=session["races"],
                dqs=session["dqs"],
                avg_wpm=session["avgWPM"],
                top_wpm=session["topWPM"],
                avg_accuracy=session["avgAccuracy"],
                top_accuracy=session["topAccuracy"],
                perfect_accuracy=session["perfectAccuracy"],
                ppr=session["ppr"],
                top_racers_rank=session["topRacersRank"]
            )
            for session in resp.json()["ongoingSessions"]
        ]
        return race_sessions

    def leaderboards_races(self, tp: TimePeriod) -> list[LeaderboardEntryRaces]:
        resp: Response = get(
            url=KlaviaAPI.Leaderboards_Races,
            params={"tp": tp},
            headers=self.headers()
        )
        top_racers: list[LeaderboardEntryRaces] = [
            LeaderboardEntryRaces(
                racer_id=r["racerId"],
                user_name=r["userName"],
                display_name=r["displayName"],
                team=r["team"],
                rank=r["rank"],
                races=r["races"]
            )
            for r in resp.json()["topRacers"]
        ]
        return top_racers

    def leaderboards_points(self, tp: TimePeriod) -> list[LeaderboardEntryPoints]:
        resp: Response = get(
            url=KlaviaAPI.Leaderboards_Points,
            params={"tp": tp},
            headers=self.headers()
        )
        top_racers: list[LeaderboardEntryPoints] = [
            LeaderboardEntryPoints(
                racer_id=r["racerId"],
                user_name=r["userName"],
                display_name=r["displayName"],
                team=r["team"],
                rank=r["rank"],
                points=r["points"]
            )
            for r in resp.json()["topRacers"]
        ]
        return top_racers

    def leaderboards_accuracy(self, tp: TimePeriod) -> list[LeaderboardEntryAccuracy]:
        resp: Response = get(
            url=KlaviaAPI.Leaderboards_Accuracy,
            params={"tp": tp},
            headers=self.headers()
        )
        top_racers: list[LeaderboardEntryAccuracy] = [
            LeaderboardEntryAccuracy(
                racer_id=r["racerId"],
                user_name=r["userName"],
                display_name=r["displayName"],
                team=r["team"],
                rank=r["rank"],
                accuracy=float(r["accuracy"])
            )
            for r in resp.json()["topRacers"]
        ]
        return top_racers

    def leaderboards_wpm(self, tp: TimePeriod) -> list[LeaderboardEntryWpm]:
        resp: Response = get(
            url=KlaviaAPI.Leaderboards_WPM,
            params={"tp": tp},
            headers=self.headers()
        )
        top_racers: list[LeaderboardEntryWpm] = [
            LeaderboardEntryWpm(
                racer_id=r["racerId"],
                user_name=r["userName"],
                display_name=r["displayName"],
                team=r["team"],
                rank=r["rank"],
                wpm=r["wpm"]
            )
            for r in resp.json()["topRacers"]
        ]
        return top_racers
