#!/usr/bin/env poetry run python

import anthropic
from anthropic import Anthropic


def main() -> None:
    client = Anthropic()

    res = client.completions.create(
        model="claude-v1",
        prompt=f"{anthropic.HUMAN_PROMPT} how does a court case get to the Supreme Court? {anthropic.AI_PROMPT}",
        max_tokens_to_sample=1000,
    )
    print(res.completion)


main()
