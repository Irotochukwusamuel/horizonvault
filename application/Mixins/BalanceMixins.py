from operator import and_

from sqlalchemy import func, case
from submodule_models_3kle import db


class BalanceMixins(object):

    def get_balance(self, use_service_id: bool = False, filter_date=None):
        from submodule_models_3kle.models import Transaction
        from submodule_models_3kle.models.transaction import TransactionStatusEnum

        """
            In this optimized function, we use a single query with case statements to calculate the sums of 
            lodgements, disbursements, and fees based on different conditions. The case statement acts as a 
            conditional aggregation, and we use the func.sum() function to compute the sums. The final balance is 
            then calculated by subtracting the disbursements and fees from the lodgements.
            This approach reduces the number of database queries to just one, resulting in
             improved performance, especially for large datasets.
        """

        # Calculate the sums of lodgements, disbursements, and fees using a single query

        """
            when calculating lodgement funds for services then, the sender_id should reference the user_id as the sender_id is the self user moving money to himself but into a service.
        """
        query = db.session.query(
            func.sum(case([(and_(Transaction.sender_id == self.user_id, Transaction.status == TransactionStatusEnum.COMPLETED.value), Transaction.amount)], else_=0)
                     ).label(
                "lodgements_sum"),
            func.sum(case([(
                and_(Transaction.user_id == self.user_id, Transaction.status.in_(
                    [TransactionStatusEnum.PROCESSING.value, TransactionStatusEnum.PENDING.value, TransactionStatusEnum.COMPLETED.value])), Transaction.amount)], else_=0)
            ).label("disbursements_sum")

        ).filter(Transaction.channel_id == self.channel_id)

        if use_service_id:
            # search for a particular service id
            query = query.filter(Transaction.service_id == self.id)

        # Apply additional filters if filter_date is provided
        if filter_date:
            query = query.filter(Transaction.created <= filter_date)

        # Execute the query and fetch the results as a tuple
        result = query.one()
        lodgement, disbursements = result

        lodgements_total = lodgement or 0
        disbursements_total = disbursements or 0

        # Calculate the final balance
        return lodgements_total - disbursements_total
