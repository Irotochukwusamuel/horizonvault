from typing import Union

from pydantic import BaseModel


class PaginationSchema(BaseModel):
    page: int = 0
    size: int = 0
    total_pages: int = 0
    total_items: int = 0
    results: Union[list,dict]
