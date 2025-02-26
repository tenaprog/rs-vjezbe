from fastapi import HTTPException

""" Generated by AI """


def parse_year_range(year_range: str):
    """
    Parse year range strings like '2015', '2015-2016', or '2015-'.
    Handles both regular hyphen '-' and Unicode en-dash '–'.
    Converts these strings into a tuple of (start_year, end_year).
    """
    try:
        year_range = year_range.replace("–", "-")

        if "-" in year_range:
            start, end = year_range.split("-")
            start = int(start) if start else None
            end = int(end) if end else None
            return start, end
        else:
            year = int(year_range)
            return year, year
    except ValueError:
        raise HTTPException(
            status_code=400, detail=f"Invalid year format: {year_range}"
        )


def year_in_range(film_year: str, start_year: int, end_year: int):
    """
    Check if a film's year range is within the given start and end year.
    film_year: Year range of the film (e.g., '2015', '2015-2016', '2015-').
    start_year: Start year of the query range.
    end_year: End year of the query range.
    """
    film_start, film_end = parse_year_range(film_year)

    if start_year is not None and film_end is not None and film_end < start_year:
        return False
    if end_year is not None and film_start is not None and film_start > end_year:
        return False
    return True
