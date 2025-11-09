from dataclasses import dataclass
from datetime import datetime


@dataclass
class RaceSession:
    racer_id: int
    user_name: str
    team: str
    started_at: datetime
    last_race_at: datetime
    races: int
    dqs: int
    avg_wpm: float
    top_wpm: float
    avg_accuracy: float
    top_accuracy: float
    perfect_accuracy: float
    ppr: str
    top_racers_rank: int


@dataclass
class LeaderboardEntry:
    racer_id: int
    user_name: str
    display_name: str
    team: str
    rank: int


@dataclass
class LeaderboardEntryRaces(LeaderboardEntry):
    races: int


@dataclass
class LeaderboardEntryPoints(LeaderboardEntry):
    points: int


@dataclass
class LeaderboardEntryAccuracy(LeaderboardEntry):
    accuracy: float


@dataclass
class LeaderboardEntryWpm(LeaderboardEntry):
    wpm: float
