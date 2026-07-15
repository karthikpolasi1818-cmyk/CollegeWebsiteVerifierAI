import json
import os


class Progress:

    FILE = "progress.json"

    @classmethod
    def load(cls):

        if not os.path.exists(cls.FILE):

            return 0

        with open(cls.FILE, "r") as f:

            data = json.load(f)

        return data.get("last_row", 0)

    @classmethod
    def save(cls, row):

        with open(cls.FILE, "w") as f:

            json.dump(
                {
                    "last_row": row
                },
                f,
                indent=4
            )

    @classmethod
    def reset(cls):

        if os.path.exists(cls.FILE):

            os.remove(cls.FILE)