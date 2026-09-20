playwright-framework/
│
├── pyproject.toml
│
├── config/
│   ├── config.dev.yaml
│   ├── config.qa.yaml
│   └── config.prod.yaml
│
├── src/
│   │
│   ├── config/
│   │   └── config.py
│   │
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   └── home_page.py
│   │
│   ├── api/
│   │   ├── base_client.py
│   │   ├── user_client.py
│   │   └── auth_client.py
│   │
│   ├── models/
│   │   ├── requests/
│   │   │   └── user_request.py
│   │   │
│   │   └── responses/
│   │       └── user_response.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── ...
│   │
│   └── constants/
│       └── ...
│
├── tests/
│   │
│   ├── conftest.py
│   │
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_home.py
│   │
│   └── api/
│       └── test_users.py
│
├── test-data/
│   ├── ui/
│   └── api/
│
└── reports/