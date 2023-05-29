from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User
from app.models.donation import Donation
from app.schemas.donation import DonationCreate, DonationUpdate
from app.services.investments import invest_donation


class CRUDdonation(CRUDBase[
    Donation,
    DonationCreate,
    DonationUpdate
]):

    async def create(
            self,
            obj_in: DonationCreate,
            session: AsyncSession,
            user: Optional[User]
    ) -> Donation:
        donation = await super().create(obj_in, session, user)
        donation = await invest_donation(donation, session)
        await session.commit()
        await session.refresh(donation)
        return donation


donation_crud = CRUDdonation(Donation)
