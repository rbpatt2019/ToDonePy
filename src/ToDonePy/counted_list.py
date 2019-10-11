from typing import List


def counted_list(lines: List[List[str]], number: int, connector: str) -> List[str]:
    """Safely iterate over lists of unknown length

    :lines: List containing items to be echoed
    :number: Number of strings to be echoed
    :connector: For pretty printing. What to join entries with

    :returns: List of lines for echoing

    """
    hold = [connector.join(line) for line in lines]
    if len(hold) > number:
        return hold[:number]
    elif len(hold) < number:
        hold.append(f"You do not have {number} tasks!")
        return hold
    else:
        return hold
