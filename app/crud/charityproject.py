from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User
from app.models.charity_project import CharityProject
from app.schemas.charityproject import (CharityProjectCreate,
                                        CharityProjectUpdate)
from app.services.investments import invest_in_charityproject


class CRUDCharityProject(CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
]):

    async def create(
            self,
            obj_in: CharityProjectCreate,
            session: AsyncSession,
            user: Optional[User] = None
    ) -> CharityProject:
        charityproject = await super().create(obj_in, session, user)
        charityproject = await invest_in_charityproject(
            charityproject,
            session,
        )
        await session.commit()
        await session.refresh(charityproject)
        return charityproject


charityproject_crud = CRUDCharityProject(CharityProject)
