from typing import List
from application.models import *
from application.models.investments import InvestmentStatus, InvestmentInterval
import datetime


def get_total_hours(interval: InvestmentInterval) -> int:
    interval_to_hours = {
        InvestmentInterval.DAILY: 24,
        InvestmentInterval.WEEKLY: 7 * 24,
        InvestmentInterval.BIWEEKLY: 2 * 7 * 24,
        InvestmentInterval.MONTHLY: 30 * 24,
        InvestmentInterval.YEARLY: 365 * 24,
        InvestmentInterval.TRIDAYS: 3 * 24,
        InvestmentInterval.BIDAYS: 2 * 24,
    }
    return interval_to_hours.get(interval, None)


def run_jobs():
    print("Running jobs...")
    investment: List[Investment] = Investment.query.filter(Investment.status == InvestmentStatus.APPROVED).all()
    for each in investment:
        maturity_date = datetime.datetime.fromtimestamp(each.created_at)
        user = each.user
        interval = each.scheme.interval
        today = datetime.datetime.today()
        time_difference = today - maturity_date
        total_hours = round(time_difference.total_seconds() / 3600)
        maturity_hours = get_total_hours(interval)
        print(f"{user} has {maturity_hours} hours of maturity")
        if maturity_hours and total_hours >= maturity_hours:
            usdt_coin: Coins = Coins.query.filter(Coins.id == 6).first()
            usdt_wallet: Wallet = Wallet.query.filter(Wallet.coin_id == usdt_coin.id, Wallet.user_id == user.id).first()
            usdt_wallet.balance += each.amount
            usdt_wallet.save()
            each.status = InvestmentStatus.COMPLETED
            each.save()
    print("Completed Investment jobs.")


run_jobs()
