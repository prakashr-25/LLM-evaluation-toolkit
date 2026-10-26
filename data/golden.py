tickets = [
    ("Charged twice for my invoice", "Billing", "High"),
    ("Send me my payment receipt", "Billing", "Low"),
    ("Card charged but payment failed", "Billing", "High"),
    ("Change my billing address", "Billing", "Low"),
    ("Discount missing from invoice", "Billing", "Medium"),

    ("Production API returns 500 errors", "Technical", "High"),
    ("How do I enable dark mode?", "Technical", "Low"),
    ("Dashboard freezes repeatedly", "Technical", "Medium"),
    ("Attachment upload is failing", "Technical", "Medium"),
    ("Service is down for all users", "Technical", "High"),

    ("Someone accessed my account", "Account", "High"),
    ("Change my account email", "Account", "Low"),
    ("Two factor login code not arriving", "Account", "High"),
    ("I want to close my account", "Account", "Medium"),
    ("Update my profile name", "Account", "Low")
]

resumes = [
    ("Asha knows Python and SQL with 2 years of experience.",
     {"name": "Asha", "skills": ["Python", "SQL"], "years_experience": 2}),

    ("Ravi has 4 years of experience using Excel and Power BI.",
     {"name": "Ravi", "skills": ["Excel", "Power BI"], "years_experience": 4}),

    ("Meena worked with Java and Spring Boot for 3 years.",
     {"name": "Meena", "skills": ["Java", "Spring Boot"], "years_experience": 3}),

    ("Fatima has 5 years of experience with Zendesk and CRM.",
     {"name": "Fatima", "skills": ["Zendesk", "CRM"], "years_experience": 5}),

    ("Arjun knows HTML, CSS and JavaScript with 1 year of experience.",
     {"name": "Arjun", "skills": ["HTML", "CSS", "JavaScript"], "years_experience": 1})
]

problems = [
    ("Three notebooks cost 45 each and two pens cost 15 each. Total?", 165),
    ("120 apples minus 35 sold plus 18 received minus 7 spoiled?", 96),
    ("Travel 60 km/h for 2 hours and 40 km/h for 3 hours. Total distance?", 240),
    ("Price 500, discount 20%, then add 18% tax. Final price?", 472),
    ("5 workers make 40 boxes in 2 days. How many can 8 make in 3 days?", 96)
]