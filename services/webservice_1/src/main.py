import random

from fastapi import FastAPI

import lib1.decider as decider

app = FastAPI()


@app.get("/")
def read_root(a: decider.Hand) -> bool | None:
    return {"status": "ok"}


@app.get("/play")
def play(a: decider.Hand) -> bool | None:
    b = random.choice([decider.Hand.ROCK, decider.Hand.PAPER, decider.Hand.SCISSORS])
    return decider.decide(a, b)
