response_deep = [
    {
        "Name": {
            "id": 0,
            "name": "anderii",
            "age": 32,
            "skills": None,
            "isPersonWork": True,

            # вкладений профіль
            "profile": {
                "contacts": {
                    "email": "andrii@example.com",
                    "phones": ["+380501112233", None],
                    "telegram": {"username": "@andrii_dev", "verified": False},
                },
                "location": {
                    "country": "UA",
                    "city": "Kyiv",
                    "geo": {"lat": 50.4501, "lng": 30.5234},
                },
            },

            # історія компаній
            "work_history": [
                {"company": "X", "role": "QA", "years": 2},
                {"company": "Y", "role": "AQA", "years": 1, "stack": ["pytest", "requests"]},
            ],

            # “зв’язки” (посилання на інші id)
            "relations": {
                "manager_id": 3,
                "teammate_ids": [1, 2],
            },
        }
    },

    {
        "Name": {
            "id": 1,
            "name": "John",
            "age": 23,
            "skills": ["Python", "Java"],
            "isPersonWork": False,

            "profile": {
                "contacts": {
                    "email": None,  # None-пастка
                    "phones": [],
                },
                "location": None,  # None-пастка
            },

            "education": [
                {"school": "Uni A", "degree": "BS", "year": 2023},
                {"school": "Course B", "degree": None, "year": "2024"},  # year як str (пастка)
            ],

            "relations": {
                "manager_id": 3,
                "mentor_id": 2,
            },
        }
    },

    {
        "Name": {
            "id": 2,
            "name": "Viktor",
            "age": 45,
            "skills": ["Python", "Java"],
            "isPersonWork": False,

            # skills деталізовані (вкладені списки словників)
            "skills_details": [
                {"name": "Python", "level": "senior", "years": 10, "tags": ["api", "automation"]},
                {"name": "Java", "level": "mid", "years": 4, "tags": None},  # tags None
            ],

            "profile": {
                "contacts": {
                    "email": "viktor@example.com",
                    "phones": ["+48100100200"],
                },
                "location": {"country": "PL", "city": "Warsaw"},
            },

            # вкладені задачі з підзадачами
            "tasks": [
                {
                    "id": "T-1",
                    "title": "Create tests",
                    "status": "done",
                    "subtasks": [
                        {"id": "T-1.1", "status": "done"},
                        {"id": "T-1.2", "status": "todo"},
                    ],
                }
            ],
        }
    },

    {
        "Name": {
            "id": 3,
            "name": "Den",
            "age": 60,
            "skills": [],  # порожній список
            "isPersonWork": True,

            "profile": {
                "contacts": {
                    "email": "den@example.com",
                    "phones": ["+123", "+456"],
                },
                "location": {"country": "UA", "city": "Lviv"},
            },

            # “керує” людьми, але тут можуть бути id яких немає (пастка)
            "manages_ids": [0, 1, 99],
        }
    },

    {
        "Name": {
            "id": 4,
            "name": "Evgen",
            "age": 30,
            "skills": None,

            # ПАСТКА: isPersonWork інколи bool, а тут dict (як у твоєму прикладі)
            "isPersonWork": {
                "id": 3,
                "name": "Den",
                "age": 60,
                "isPersonWork": True,
            },

            "profile": {
                "contacts": {
                    "email": "evgen@example.com",
                    "phones": ["+380777777777"],
                    "telegram": {"username": None, "verified": "yes"},  # verified як str
                },
                "location": {"country": "UA", "city": None},  # city None
            },

            # Вкладений “проект” з учасниками
            "projects": [
                {
                    "name": "Project A",
                    "members": [
                        {"person_id": 0, "role": "lead"},
                        {"person_id": 1, "role": "dev"},
                    ],
                    "meta": {"budget": 10000, "currency": "USD"},
                },
                {
                    "name": "Project B",
                    "members": None,  # пастка
                    "meta": {"budget": "unknown"},  # пастка
                },
            ],
        }
    },
]
