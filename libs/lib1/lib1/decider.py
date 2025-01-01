import enum

class Hand(enum.StrEnum):
    ROCK = enum.auto()
    PAPER = enum.auto()
    SCISSORS = enum.auto()


def decide(a: Hand, b: Hand) -> bool | None:
    """
    Returns True if the first hand beats
    the second, False if it is the other way
    around and None if there is a tie.
    """
    if a == b:
        return
    return _RULES[(a, b)]


_RULES = {
    (Hand.ROCK, Hand.PAPER): False,
    (Hand.ROCK, Hand.SCISSORS): True,
    (Hand.PAPER, Hand.ROCK): True,
    (Hand.PAPER, Hand.SCISSORS): False,
    (Hand.SCISSORS, Hand.ROCK): False,
    (Hand.SCISSORS, Hand.PAPER): True,

}