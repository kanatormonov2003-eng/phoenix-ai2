from pathlib import Path


def load_knowledge():

    knowledge = ""

    folder = Path("knowledge")

    for file in folder.glob("*.md"):
        knowledge += f"\n\n--- {file.name} ---\n"
        knowledge += file.read_text(encoding="utf-8")

    return knowledge