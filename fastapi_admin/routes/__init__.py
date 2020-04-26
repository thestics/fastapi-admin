from fastapi import Depends

from . import login, site, index
from ..depends import jwt_required
from ..factory import app

app.include_router(login.router)
app.include_router(site.router)
app.include_router(index.router, dependencies=[Depends(jwt_required)], prefix='/rest')
