from importlib import import_module
from logging import getLogger
from pathlib import Path

from src.templating import Actor
from src.weighted_random import WeightedList

log = getLogger("character-init")

characters: WeightedList[Actor] = WeightedList()

for file in Path(__file__).parent.glob("*.chr.py"):
    if not file.is_file() or file.name == __file__:
        continue

    try:
        characters.append(character := import_module(file.name).character)
        log.debug("Loaded {character.name} character from {file}.")
    except Exception:
        log.exception("Character file {file} is invalid. Skipping.")
        continue
