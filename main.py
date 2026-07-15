"""
main.py

College Website Verifier AI
Production Version
"""

from config import INPUT_FILE, OUTPUT_FILE, SAVE_EVERY
from utils.excel import ExcelReader
from exporter.excel_writer import ExcelWriter
from pipeline import Pipeline
from utils.progress import Progress
from utils.logger import logger
from crawler.browser import Browser


def main():

    logger.info("=" * 80)
    logger.info("College Website Verifier AI Started")
    logger.info("=" * 80)

    browser = Browser()

    try:
        browser.start()

        reader = ExcelReader(INPUT_FILE)
        colleges = reader.get_colleges()
        total = len(colleges)

        logger.info(f"Loaded {total} colleges")

        writer = ExcelWriter(INPUT_FILE, OUTPUT_FILE)
        writer.create_columns()

        pipeline = Pipeline()

        start = 0
        logger.info(f"Starting from row {start + 1}")

        for index in range(start, total):

            college = colleges[index]

            logger.info("")
            logger.info("=" * 80)
            logger.info(f"{index + 1}/{total}")
            logger.info(college)
            logger.info("=" * 80)

            try:
                result = pipeline.process(college)

                print("\n" + "=" * 80)
                print("RESULT RETURNED BY PIPELINE")
                print("=" * 80)
                print(result)

            except KeyboardInterrupt:
                logger.warning("Interrupted by user.")
                writer.save()
                Progress.save(index)
                return

            except Exception as e:
                logger.exception(e)

                result = {
                    "website": "",
                    "title": "",
                    "confidence": 0,
                    "verified": False,
                    "social": {},
                    "emails": [],
                    "phones": [],
                    "addresses": [],
                    "pages": {},
                }

            writer.update(index, result)
            print(f"Written row {index + 1}")

            writer.save()
            Progress.save(index + 1)

            if (index + 1) % SAVE_EVERY == 0:
                logger.info("Saving checkpoint...")
                writer.save()
                logger.info("Checkpoint Saved")

        writer.save()
        Progress.reset()

        logger.info("=" * 80)
        logger.info("Completed Successfully")
        logger.info("=" * 80)

    except KeyboardInterrupt:
        logger.warning("Program stopped by user.")

    finally:
        try:
            browser.stop()
        except Exception:
            pass


if __name__ == "__main__":
    main()
