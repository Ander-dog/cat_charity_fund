from datetime import datetime
from typing import Tuple, Union

from sqlalchemy import false, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


def close(
        closing_obj: Union[CharityProject, Donation],
        session: AsyncSession
) -> Union[CharityProject, Donation]:
    closing_obj.invested_amount = closing_obj.full_amount
    closing_obj.fully_invested = True
    closing_obj.close_date = datetime.now()
    session.add(closing_obj)
    return closing_obj


def investment(
        donation: Donation,
        project: CharityProject,
        session: AsyncSession
) -> Tuple[Donation, CharityProject]:
    donation_money = donation.full_amount - donation.invested_amount
    requested_money = project.full_amount - project.invested_amount
    if donation_money > requested_money:
        donation.invested_amount += requested_money
        session.add(donation)
        close(project, session)
    elif donation_money < requested_money:
        project.invested_amount += donation_money
        session.add(project)
        close(donation, session)
    else:
        close(donation, session)
        close(project, session)
    return donation, project


async def invest_donation(
        donation: Donation,
        session: AsyncSession,
) -> Donation:
    while not donation.fully_invested:
        project = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == false()
            )
        )
        project = project.scalars().first()
        if project is None:
            break
        donation, project = investment(donation, project, session)
    return donation


async def invest_in_charityproject(
        project: CharityProject,
        session: AsyncSession,
) -> CharityProject:
    while not project.fully_invested:
        donation = await session.execute(
            select(Donation).where(Donation.fully_invested == false())
        )
        donation = donation.scalars().first()
        if donation is None:
            break
        donation, project = investment(donation, project, session)
    return project
