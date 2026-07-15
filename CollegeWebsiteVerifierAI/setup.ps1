$folders = @(
    "data",
    "output",
    "logs",
    "search",
    "search\providers",
    "search\filters",
    "crawler",
    "crawler\browsers",
    "crawler\pages",
    "llm",
    "llm\agents",
    "llm\prompts",
    "linkedin",
    "linkedin\search",
    "linkedin\verify",
    "database",
    "utils",
    "validators",
    "validators\rules",
    "extractors",
    "extractors\emails",
    "extractors\phones",
    "extractors\address",
    "extractors\social",
    "exporters",
    "exporters\excel",
    "exporters\json",
    "prompts",
    "models",
    "tests",
    "tests\search",
    "tests\crawler",
    "tests\llm",
    "cache",
    "reports",
    "docs",
    "config"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

$files = @(
    "main.py",
    "config.py",
    ".env",
    "requirements.txt",
    "README.md",

    "search\__init__.py",
    "search\search_api.py",
    "search\google_search.py",
    "search\tavily_search.py",
    "search\serpapi_search.py",
    "search\result_filter.py",
    "search\website_ranker.py",

    "crawler\__init__.py",
    "crawler\browser.py",
    "crawler\crawler.py",
    "crawler\extractor.py",
    "crawler\social_links.py",
    "crawler\contact_page.py",
    "crawler\about_page.py",
    "crawler\placement_page.py",

    "llm\__init__.py",
    "llm\verifier.py",
    "llm\confidence.py",
    "llm\prompt_builder.py",
    "llm\response_parser.py",

    "linkedin\__init__.py",
    "linkedin\linkedin_search.py",
    "linkedin\linkedin_verify.py",
    "linkedin\linkedin_parser.py",

    "database\__init__.py",
    "database\database.py",
    "database\models.py",
    "database\progress.py",

    "utils\__init__.py",
    "utils\logger.py",
    "utils\helpers.py",
    "utils\retry.py",
    "utils\validators.py",
    "utils\excel.py",
    "utils\constants.py",

    "validators\website_validator.py",
    "validators\linkedin_validator.py",
    "validators\domain_validator.py",
    "validators\confidence_score.py",

    "extractors\emails\email_extractor.py",
    "extractors\phones\phone_extractor.py",
    "extractors\address\address_extractor.py",
    "extractors\social\social_extractor.py",

    "exporters\excel\excel_writer.py",
    "exporters\json\json_writer.py",

    "prompts\website_prompt.txt",
    "prompts\linkedin_prompt.txt",
    "prompts\verification_prompt.txt",

    "tests\search\test_search.py",
    "tests\crawler\test_crawler.py",
    "tests\llm\test_llm.py"
)

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
    }
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Green
Write-Host " Project Structure Created Successfully!" -ForegroundColor Green
Write-Host "===================================" -ForegroundColor Green