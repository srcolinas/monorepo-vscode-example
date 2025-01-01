import pytest

from lib1.decider import Hand, decide


@pytest.mark.parametrize(
    "a,b,result",
    [
        (Hand.ROCK, Hand.ROCK, None),
        (Hand.ROCK, Hand.PAPER, False),
        (Hand.ROCK, Hand.SCISSORS, True),
        (Hand.PAPER, Hand.ROCK, True),
        (Hand.PAPER, Hand.PAPER, None),
        (Hand.PAPER, Hand.SCISSORS, False),
        (Hand.SCISSORS, Hand.ROCK, False),
        (Hand.SCISSORS, Hand.PAPER, True),
        (Hand.SCISSORS, Hand.SCISSORS, None),
    ],
)
def test_decisions(a: Hand, b: Hand, result: bool | None):
    assert decide(a, b) == result
