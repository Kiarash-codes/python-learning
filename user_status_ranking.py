users = "Ali": {"level": 15, "score": 250},"Sara": {"level": 8, "score": 120},"Reza": {"score": 300},"Mina": {"level": 10}}

for name, info in users.items():
    if info.get("level", 0) >= 10:
        status = "PRO"
    else:
        status = "BEGINNER"
    info.update({"status": status})

    if info.get("score", 0) >= 200:
        info.update({"rank": "High Score"})
    else:
        info.update({"rank": "Normal Score"})
removed_score = users["Sara"].pop("score")
print(removed_score)
print(users)
