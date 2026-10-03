# Media Monitoring: Keyword-Based News Alerts

A Python tool that **scrapes a news portal**, indexes article links and content, matches them against **keywords subscribed by clients**, and **emails each client** the news that mentions their keywords.

## How it works
```
News portal ──► Scrapper (links) ──► Content extractor ──► media_link.json
                                                                │
Client list (Excel ──► JSON: email, keywords, period) ──► Keyword matcher
                                                                │
                                              data_flow.json ──► MailSender (SMTP) ──► client inbox
```

1. **Scrape** the portal's front page and collect article links.
2. **Extract** each article's text (from `<p>` / `<span>` content).
3. **Load clients** from an Excel sheet (converted to JSON): email, keywords and time period (currently 1 by default).
4. **Match** every client keyword against article links and content.
5. **Build a data flow** per client (which links matched which keywords) and save it to JSON.
6. **Send an email** to each client with their matched news.

## Tech stack
`Python 3` `requests` `pandas` (Excel → JSON) `SMTP (Gmail)` · JSON files as lightweight storage

## Project structure
```
media/
├── main.py                    # Orchestrates scrape → match → email
├── component/
│   ├── scrapper.py            # Collects article links
│   ├── search.py              # Extracts content, matches keywords, builds email payload
│   ├── excel_handler.py       # Excel → JSON client import
│   ├── repository.py          # JSON persistence (links, data flows)
│   ├── mail_sender.py         # SMTP email sender
│   └── settings.py            # Paths, portal URL, mail config
├── database_tables/           # JSON "tables": links, clients, keywords, data flows
├── excel/                     # Client subscription sheet
└── examples/                  # Sample input/output JSON
```

## Running
```bash
pip install -r requirements.txt
python main.py
```

Mail credentials are read from an external config file (INI format, `[CREDENTIALS]` section with `email` and `password`). Point `component/settings.py` to your own file. Credentials are not stored in this repository.

## Possible improvements
- Schedule runs (cron / APScheduler) and support per-client time periods
- Replace JSON files with a database (SQLite/PostgreSQL)
- Async scraping (aiohttp) and duplicate-article detection
- HTML email templates
