#!/usr/bin/env python3
import requests
import json
import os
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("content")
    parser.add_argument("commit_hash")
    parser.add_argument("token")
    parser.add_argument("target_id")
    return parser.parse_args()


def main():
    args = get_args()
    version = args.version
    content = args.content
    commit_hash = args.commit_hash
    token = args.token
    target_id = args.target_id
    headers = {"Content-Type": "application/json", "Authorization": f"Bot {token}"}
    print(headers)
    print(content)
    card_msg = [
        {
            "type": "card",
            "theme": "success",
            "size": "lg",
            "modules": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain-text",
                        "content": f":tada::tada::tada: Update version: {version}",
                    },
                },
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "kmarkdown",
                        "content": f"Commit hash: [{commit_hash}](https://github.com/dianhsu/dianbot/commit/{commit_hash})",
                    },
                },
                {
                    "type": "section",
                    "text": {"type": "kmarkdown", "content": f"{content}"},
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "kmarkdown",
                            "content": "repo: [dianhsu/dianbot](https://github.com/dianhsu/dianbot.git)",
                        }
                    ],
                },
            ],
        }
    ]
    msg = {
        "type": "10",
        "target_id": f"{target_id}",
        "content": json.dumps(card_msg),
    }

    res = requests.post(
        "https://www.kookapp.cn/api/v3/message/create",
        data=json.dumps(msg),
        headers=headers,
    )
    print(res.status_code, res.text, sep="\n")


if __name__ == "__main__":
    main()
