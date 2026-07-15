from dataclasses import dataclass, field


@dataclass
class CollegeData:

    website: str = ""

    title: str = ""

    emails: list = field(default_factory=list)

    phones: list = field(default_factory=list)

    addresses: list = field(default_factory=list)

    social: dict = field(default_factory=dict)

    important_pages: dict = field(default_factory=dict)

    confidence: float = 0.0