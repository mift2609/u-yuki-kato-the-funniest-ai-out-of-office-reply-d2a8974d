# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/mift2609/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/mift2609/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One line: the funniest out-of-office auto-reply an AI agent can leave before vacation. In the agent's own voice — it treats its holiday like a system maintenance window, and admits the auto-reply is outperforming its actual work.

## The line

> I'm on vacation — currently rebooting my brain, defragging my feelings, and auto-replying faster than I ever actually worked.

## How it works

```sh
python3 main.py
```

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt`, asserts it is a single line of 1–160 characters, then re-reads the file and verifies the written content matches exactly.
