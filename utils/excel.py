import pandas as pd


class ExcelReader:

    def __init__(self, file_path):

        self.file_path = file_path

        # Load immediately
        self.df = pd.read_excel(file_path)

    def get_colleges(self):

        # Possible column names
        possible_columns = [
            "Institute Name",
            "College Name",
            "Name",
            "Institute",
            "College",
        ]

        column = None

        for col in possible_columns:
            if col in self.df.columns:
                column = col
                break

        if column is None:
            raise ValueError(
                f"No college name column found.\n"
                f"Available columns:\n{list(self.df.columns)}"
            )

        return (
            self.df[column]
            .dropna()
            .astype(str)
            .str.strip()
            .tolist()
        )