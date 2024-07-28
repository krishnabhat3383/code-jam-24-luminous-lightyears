"""Import and store all the characters and templates for use."""

from importlib import import_module
from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING

from src.weighted_random import WeightedList

if TYPE_CHECKING:
    from src.templating import Actor

log = getLogger("character-init")

all_characters: WeightedList["Actor"] = WeightedList()

for file in Path(__file__).parent.glob("*.py"):
    module = file.name.split(".")[0]

    if not file.is_file() or not module.endswith("_chr"):
        continue

    try:
        all_characters.append(character := import_module(f"src.characters.{module}").character)
        log.debug("Loaded %s character from %s.", character.name, file)
    except Exception:
        log.exception("Character file %s is invalid. Skipping.", file)
        continue
