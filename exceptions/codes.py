from enum import Enum


class ExceptionCode(Enum):
    """
        ERROR TYPE : GENERIC ERRORS
        CODE : 19
        DESCRIPTION : GENERIC ERROR USED ON THE SYSTEM.
        ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
    """
    UNAVAILABLE_SERVICE = {'response_code': 1999, 'message': 'Unavailable service, please try again', 'status_code': 400}
    INVALID_TRANSACTION_AMOUNT = {'response_code': 1998, 'message': 'Invalid transaction amount', 'status_code': 400}
    ACCOUNT_BLOCKED = {'response_code': 1997, 'message': 'Account blocked', 'status_code': 400}
    EXPIRED_TOKEN = {'response_code': 1996, 'message': 'Expired token', 'status_code': 401}
    INVALID_ACCOUNT_TYPE = {'response_code': 1995, 'message': 'Invalid account type', 'status_code': 400}
    INVALID_PIN = {'response_code': 1994, 'message': 'Invalid PIN', 'status_code': 400}
    SERVICE_UNAVAILABLE = {'response_code': 1993, 'message': 'Service unavailable', 'status_code': 503}
    NETWORK_ERROR = {'response_code': 1992, 'message': 'Network error', 'status_code': 500}
    BLOCKED_CARD = {'response_code': 1991, 'message': 'Card blocked', 'status_code': 400}
    UNAUTHORIZED_ACCESS = {'response_code': 1990, 'message': 'You are not authorized to execute this request.',
                           'status_code': 401}
    INVALID_FORMAT = {'response_code': 1989, 'message': 'Invalid data format', 'status_code': 400}
    TIMEOUT_ERROR = {'response_code': 1988, 'message': 'Request timeout', 'status_code': 408}
    SERVER_UNAVAILABLE = {'response_code': 1987, 'message': 'Server unavailable', 'status_code': 503}
    INACTIVE_ACCOUNT = {'response_code': 1986, 'message': 'Inactive account', 'status_code': 400}
    CARD_DECLINED = {'response_code': 1985, 'message': 'Card declined', 'status_code': 400}
    UNSUPPORTED_OPERATION = {'response_code': 1984, 'message': 'Unsupported operation', 'status_code': 400}
    LIMIT_EXCEEDED = {'response_code': 1983, 'message': 'Transaction limit exceeded', 'status_code': 400}
    LOCKED_ACCOUNT = {'response_code': 1982, 'message': 'Account locked', 'status_code': 400}
    INVALID_CREDENTIALS = {'response_code': 1981,
                           'message': 'Your username and/or password is incorrect. Please try again with correct credentials.',
                           'status_code': 401}
    DUPLICATE_TRANSACTION = {'response_code': 1980, 'message': 'Duplicate transaction', 'status_code': 400}
    CARD_EXPIRED = {'response_code': 1979, 'message': 'Card expired', 'status_code': 400}
    INVALID_TRANSACTION = {'response_code': 1978, 'message': 'Invalid transaction', 'status_code': 400}
    TRANSACTION_FAILED = {'response_code': 1977, 'message': 'Transaction failed', 'status_code': 400}
    ACCOUNT_NOT_FOUND = {'response_code': 1976, 'message': 'Account not found', 'status_code': 404}
    INSUFFICIENT_FUNDS = {'response_code': 1975, 'message': 'Insufficient funds', 'status_code': 400}
    AUTHENTICATION_FAILED = {'response_code': 1974, 'message': 'You must be log in first to execute this request.',
                             'status_code': 401}
    INVALID_INPUT = {'response_code': 1973, 'message': 'Invalid input', 'status_code': 400}
    DATABASE_ERROR = {'response_code': 1972, 'message': 'Database error', 'status_code': 400}
    INVALID_REQUEST = {'response_code': 1971, 'message': 'Invalid request', 'status_code': 400}
    RESOURCE_NOT_FOUND = {'response_code': 1970, 'message': 'Resource not found', 'status_code': 404}
    ATTRIBUTES_MISSING = {'response_code': 1969, 'message': 'One the following values must be supplied: {attributes}',
                          'status_code': 400}
    INVALID_TRANSACTION_PIN = {'response_code': 1968, 'message': 'Invalid transaction pin', 'status_code': 403}
    LOAN_EXIST = {'response_code': 1967, 'message': 'User already has a loan', 'status_code': 400}
    WALLET_NOT_FOUND = {'response_code': 1966, 'message': 'No wallets were found for this user', 'status_code': 400}
    ADMIN_ACCESS_REQUIRED = {'response_code': 1965, 'message': 'Only an admin can perform this action.',
                             'status_code': 401}
    PIN_NOT_VERIFIED = {'response_code': 1964, 'message': 'Please verify your pin', 'status_code': 400}
    INVALID_DATE_FORMAT = {'response_code': 1963, 'message': 'Please provide date in YYYY-MM-DD format',
                           'status_code': 400}
    INVALID_VISA_CURRENCY_DESTINATION = {'response_code': 1962,
                                         'message': "Source or destination currency you've provided is invalid. Please try again with correct currency code.",
                                         'status_code': 400}
    VISA_CONNECTION_ERROR = {'response_code': 1961,
                             'message': "There's some error connecting to visa pay client. Please try again later.",
                             'status_code': 500}
    PHONE_NOT_VERIFIED = {'response_code': 1960, 'message': 'Phone could not be verified. Please check phone number',
                          'status_code': 400}
    OTP_INCORRECT = {'response_code': 1959, 'message': 'Phone could not be verified. Otp is incorrect',
                     'status_code': 400}
    OTP_EXPIRED = {'response_code': 1958,
                   'message': 'Phone could not be verified. Otp has been expired. Please request for new otp',
                   'status_code': 400}
    PHONE_NOT_VERIFIED_NOT_PERFORMED = {'response_code': 1957, 'message': "Please complete phone verification first.",
                                        'status_code': 400}
    PHONE_VERIFICATION_NOT_COMPLETED = {'response_code': 1956,
                                        'message': 'You can not complete this step. Please verify phone number first.',
                                        'status_code': 400}
    PHONE_VERIFICATION_NOT_COMPLETED_INVALID_EMAIL = {'response_code': 1955,
                                                      'message': 'Phone verification could not completed. Please enter valid email.',
                                                      'status_code': 400}
    CORRUPTED_DOCUMENT = {'response_code': 1954, 'message': 'Document you uploaded is corrupted.', 'status_code': 415}
    LESS_THAN_18 = {'response_code': 1953, 'message': 'User is less than 18 years', 'status_code': 400}
    INCOMPLETE_BASIC_INFO = {'response_code': 1952, 'message': "User hasn't completed basic information",
                             'status_code': 400}
    ACCOUNT_INACTIVE = {'response_code': 1951, 'message': 'User is currently not active', 'status_code': 400}
    ACCOUNT_NUMBER_NOT_FOUND = {'response_code': 1950, 'message': 'User does not have individual account number',
                                'status_code': 400}
    INVALID_STATE_ID = {'response_code': 1949, 'message': 'Please pass a state id', 'status_code': 400}
    USER_EXISTS = {'response_code': 1948,
                   'message': 'A user with the given email/ phone already exists. Please try logging in using those details.',
                   'status_code': 401}
    TRANSACTION_NOT_FOUND = {'response_code': 1947, 'message': 'No Transaction found', 'status_code': 400}
    INVALID_TOKEN = {'response_code': 1946, 'message': 'The token supplied is invalid', 'status_code': 403}
    INVALID_AUTHORIZATION_URL = {'response_code': 1945, 'message': 'The authorization url supplied is invalid',
                                 'status_code': 400}
    INVALID_FUNDING_SOURCE = {'response_code': 1944, 'message': 'Invalid funding source, must be: personal or business',
                              'status_code': 400}
    KYC_NOT_VERIFIED = {'response_code': 1943, 'message': 'KYC is not verified',
                        'status_code': 400}
    CHANNEL_NOT_FOUND = {'response_code': 1942, 'message': 'This channel does not exist, please select a valid channel',
                         'status_code': 404}
    DATA_MISMATCH = {'response_code': 1941, 'message': "Data mismatch, {attr_a} and {attr_b} do not match"}
    BAD_REQUEST = {'response_code': 1940, 'message': 'Bad Request!', 'status_code': 400}
    KYC_ALREADY_EXISTS = {'response_code': 1939, 'message': 'KYC exists already!', 'status_code': 400}
    INVALID_PAGE_NUMBER = {'response_code': 1938, 'message': 'Invalid page number', 'status_code': 400}
    PERMISSION_DENIED = {'response_code': 1937, 'message': 'Permission denied', 'status_code': 403}

    '''
        ERROR TYPE : SUBSCRIPTION ERRORS
        CODE : 18
        DESCRIPTION : SUBSCRIPTION ERROR USED ON THE SYSTEM.
        ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
    '''

    NO_ACTIVE_SUBCRIPTION = {'response_code': 1899, 'message': 'You have no active subscription', 'status_code': 400}
    SUBSCRIPTION_EXPIRED = {'response_code': 1898, 'message': 'Subscription expired', 'status_code': 403}
    INVALID_PLAN = {'response_code': 1897, 'message': 'Invalid plan', 'status_code': 400}
    NO_SUBSCRIPTION_ACCESS = {'response_code': 1896,
                              'message': 'Sorry, this service is not available on your subscription plan.',
                              'status_code': 400}
    NO_PREVIOUS_SUBSCRIPTION = {'response_code': 1896, 'message': "You have no previous payments", 'status_code': 400}

    '''
          ERROR TYPE : TRANSACTIONS ERRORS
          CODE : 17
          DESCRIPTION : TRANSACTIONS ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    ONLY_ONE_SENDER_REQUIRED = {'response_code': 1799, 'message': 'A transaction can have only one sender',
                                'status_code': 400}
    ONLY_ONE_RECEIVER_REQUIRED = {'response_code': 1798, 'message': 'A transaction can have only one receiver',
                                  'status_code': 400}
    INVALID_SELF_SENDER = {'response_code': 1797, 'message': 'Money cannot be sent to self', 'status_code': 400}
    INVALID_TRIKLE_PAY = {'response_code': 1796, 'message': 'Link is not valid. Please enter valid trikle_pay_id.',
                          'status_code': 400}
    INVALID_ACCESS_CODE = {'response_code': 1795, 'message': 'Invalid access code.', 'status_code': 400}
    SELF_TRANSFER_NOT_PROCESSED = {'response_code': 1794,
                                   'message': "Request not processed! You can\'t do self transfer.", 'status_code': 400}
    LINK_EXPIRED = {'response_code': 1793, 'message': 'Link has expired!', 'status_code': 400}
    INVALID_TRIKLE_LINK = {'response_code': 1792, 'message': 'Link is not valid. Please enter valid trikle_pay_id.',
                           'status_code': 400}
    UNABLE_TO_VALIDATE_RECEIVE_BANK = {'response_code': 1791,
                                       'message': 'Unable to validate receiver\'s bank account. Please provide correct input.',
                                       'status_code': 400}
    INVALID_WITHDRAW_DESTINATION = {'response_code': 1790, 'message': 'Invalid withdraw destination',
                                    'status_code': 400}
    INVALID_SENDER_ACCOUNT = {'response_code': 1789, 'message': 'Invalid sender account',
                              'status_code': 400}
    INVALID_RECEIVER_ACCOUNT = {'response_code': 1788, 'message': 'Invalid receiver account',
                                'status_code': 400}
    AMOUNT_MUST_BE_GREATER_THAN_0 = {'response_code': 1787, 'message': 'Amount must greater than 0',
                                     'status_code': 400}

    RECEIVER_OR_SERVICE_ID_REQUIRED = {'response_code': 1786, 'message': 'The receiver account or service id is required',
                                     'status_code': 400}

    '''
        ERROR TYPE : SAVINGS ERRORS
        CODE : 16
        DESCRIPTION : SAVINGS ERROR USED ON THE SYSTEM.
        ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
    '''

    NO_SAVINGS_FOUND = {'response_code': 1699, 'message': 'No savings found', 'status_code': 400}
    AUTOSAVE_NOT_ENABLED = {'response_code': 1698, 'message': 'Auto save is not enabled', 'status_code': 400}
    INVALID_START_DATE = {'response_code': 1697, 'message': 'Invalid start date, must be after today',
                          'status_code': 400}
    FIXED_SAVINGS_NOT_ENABLED = {'response_code': 1696, 'message': 'Fixed savings not enabled, something went wrong',
                                 'status_code': 400}
    INVALID_DURATION = {'response_code': 1695, 'message': 'Invalid duration', 'status_code': 400}
    PAY_MANUALLY = {'response_code': 1694, 'message': 'Something went wrong, please pay manually', 'status_code': 500}
    NO_GOAL_SAVING_WITH_ID = {'response_code': 1693, 'message': 'No goal savings with the given id were found',
                              'status_code': 400}
    GOAL_SAVING_DISABLED = {'response_code': 1692, 'message': 'This goal savings has been disabled', 'status_code': 400}

    '''
          ERROR TYPE : GROUP SAVINGS ERRORS
          CODE : 15
          DESCRIPTION : GROUP SAVINGS ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM & REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    GROUP_NAME_EXIST = {'response_code': 1599,
                        'message': 'A group with this name already exists, please try another name', 'status_code': 400}
    GROUP_ID_NOT_EXIST = {'response_code': 1598, 'message': 'Group savings  with the provided id doesn\'t exist',
                          'status_code': 404}
    GROUP_NOT_UPDATED = {'response_code': 1597, 'message': 'Group savings not updated', 'status_code': 500}
    GROUP_CREATION_FAILED = {'response_code': 1596,
                             'message': 'Group savings could not be created at this time, please try again',
                             'status_code': 500}
    GROUP_MEMBER_NOT_PRESENT = {'response_code': 1595,
                                'message': 'Failed, member must be present in the group and in decline state',
                                'status_code': 400}
    GROUP_MEMBER_NOT_EXIST = {'response_code': 1594, 'message': 'Member doesn\'t exist', 'status_code': 404}
    PREVIOUS_GROUP_STILL_PENDING = {'response_code': 1593,
                                    'message': 'A new group cannot be created if any previously created groups are pending',
                                    'status_code': 400}
    UNAUTHORIZED_GROUP_SAVING_ACCESS = {'response_code': 1592,
                                        'message': "You are not authorised to update this group's configuration",
                                        'status_code': 400}
    GROUP_NOT_PENDING = {'response_code': 1591, 'message': "Group is not in pending state.", 'status_code': 400}
    GROUP_NOT_UPDATED_WITH_CHANGES = {'response_code': 1590, 'message': "Group savings not updated, no changes found.",
                                      'status_code': 400}
    GROUP_CAPACITY_EXCEEDED = {'response_code': 1589,
                               'message': "Group members not added, group capacity has been exceeded",
                               'status_code': 400}
    ACTIVE_MEMBER_EXIST = {'response_code': 1588, 'message': "You are already an active member", 'status_code': 400}
    EXPIRED_GROUP_INVITATION = {'response_code': 1587,
                                'message': "Invitation to this group has expired, group has left pending state.",
                                'status_code': 400}
    ALREADY_DECLINED_INVITE = {'response_code': 1586, 'message': "You have already declined this invite",
                               'status_code': 400}
    GROUP_NOT_COMPLETED = {'response_code': 1585, 'message': "Group is not in a completed state.", 'status_code': 400}
    NO_CONTRIBUTION_FOUND = {'response_code': 1584, 'message': "No contributions found",
                             'status_code': 404}
    NO_CONTRIBUTION_FOUND_ACTIVE_GROUP = {'response_code': 1583,
                                          'message': "No contributions found, group is not active", 'status_code': 404}
    NO_CONTRIBUTION_FOUND_FOR_WEEK = {'response_code': 1582,
                                      'message': "No Contributions exists found for current week", 'status_code': 404}
    NO_PAYOUT_FOUND_FOR_GROUP = {'response_code': 1581, 'message': "No payouts found",
                                 'status_code': 404}
    NO_PAYOUT_FOUND = {'response_code': 1580, 'message': "No payouts found", 'status_code': 404}
    GROUP_NOT_ACTIVE = {'response_code': 1579, 'message': "Group is not in an active state.", 'status_code': 400}
    NO_CONTRIBUTION_MADE = {'response_code': 1578, 'message': "No contributions have been made", 'status_code': 400}
    LAST_PAYMENT_COMPLETED = {'response_code': 1577, 'message': "Failed, last payment was completed successfully",
                              'status_code': 400}
    MEMBERS_MUST_BE_INTEGER = {'response_code': 1576, 'message': "number_of_members must be an integer",
                               'status_code': 400}
    SAVINGS_DURATION_MUST_BE_INTEGER = {'response_code': 1575, 'message': "savings_duration must be an integer",
                                        'status_code': 400}
    GROUP_MEMBERS_MUST_BE_2_TO_12 = {'response_code': 1574,
                                     'message': "Amount of members in a group must be within 2 - 12, both inclusive",
                                     'status_code': 400}
    NO_GROUP_MEMBERS_FOUND = {'response_code': 1573, 'message': "No group members found", 'status_code': 404}

    '''
          ERROR TYPE : ACCOUNT ERRORS
          CODE : 14
          DESCRIPTION : ACCOUNT  ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    MAXIMUM_NO_ACCOUNT_EXCEEDED = {'response_code': 1499,
                                   'message': 'The maximum number of accounts permissible per request is 10',
                                   'status_code': 400}
    NAME_NOT_FOUND = {'response_code': 1498, 'message': 'Name does not exist', 'status_code': 400}
    BANK_NOT_FOUND = {'response_code': 1497, 'message': 'Bank does not exist', 'status_code': 400}
    INACTIVE_BANK = {'response_code': 1496, 'message': 'Bank is Inactive', 'status_code': 400}
    INVALID_ACCOUNT_NUMBER = {'response_code': 1495, 'message': 'Account number must be 10 digits', 'status_code': 400}
    INVALID_DESTINATION_INSTITUTION_CODE = {'response_code': 1494,
                                            'message': 'DestinationInstitutionCode must be 6 digits',
                                            'status_code': 400}
    INVALID_BVN_NUMBER = {'response_code': 1493, 'message': 'Invalid bvn number', 'status_code': 400}
    INVALID_TRANSACTION_ID = {'response_code': 1492, 'message': 'Incorrect transaction id. Ensure length is 30',
                              'status_code': 400}
    BVN_NOT_VERIFIED = {'response_code': 1491, 'message': "BVN is not verified.", 'status_code': 400}
    OTP_WAIT_TIME = {'response_code': 1490,
                     'message': "Please try after 30 mins. You have exceeded limit for phone verification attempts.",
                     'status_code': 400}
    PROVIDE_OTP = {'response_code': 1489, 'message': "Please provide otp.", 'status_code': 400}
    ONBOARDING_COMPLETE = {'response_code': 1488, 'message': "Onboarding already completed.", 'status_code': 400}
    ACCOUNT_NOT_ADDED = {'response_code': 1487, 'message': "Your account could not be added. Please try again later.",
                         'status_code': 400}
    EMAIL_EXISTS = {'response_code': 1486, 'message': "This email already registered with other user.",
                    'status_code': 400}
    EMAIL_CANNOT_BE_CHANGED = {'response_code': 1485,
                               'message': "You cant change your email. Please verify your phone first.",
                               'status_code': 400}
    USER_NOT_UPDATED = {'response_code': 1484,
                        'message': "User record not updated in App User Model.",
                        'status_code': 400}
    REFERRAL_EXPIRED = {'response_code': 1483,
                        'message': "The referral code is expired",
                        'status_code': 400}
    INVALID_NOTIFICATION = {'response_code': 1482,
                            'message': 'Notification type provided is not valid.', 'status_code': 400}
    INVALID_PANIC_AMOUNT = {'response_code': 1481,
                            'message': 'Panic amount must be of type Number', 'status_code': 400}
    REFERRAL_INVALID = {'response_code': 1480,
                        'message': 'The referral code provided is invalid', 'status_code': 400}
    INVALID_IMAGE = {'response_code': 1479,
                     'message': 'Image uri not found. Please upload a valid image.', 'status_code': 400}
    INCOMPLETE_ONBOARD = {'response_code': 1478,
                          'message': 'User onboarding not completed', 'status_code': 400}

    ACCOUNT_ALREADY_ACTIVATED = {'response_code': 1477,
                                 'message': 'This account is already activated', 'status_code': 400}
    ACCOUNT_ALREADY_DEACTIVATED = {'response_code': 1476,
                                   'message': 'This account is already deactivated', 'status_code': 400}
    INELIGIBLE_TO_VIEW = {'response_code': 1475,
                          'message': 'You are not eligible to view this.', 'status_code': 400}
    BVN_NEEDED_FOR_BUSINESS = {'response_code': 1474,
                               'message': 'BVN is mandatory to open business account', 'status_code': 400}
    RC_TIN_NOT_VERIFIED = {'response_code': 1473,
                           'message': 'RC and Tin not verified. Please Verify first.', 'status_code': 400}
    BUSINESS_ID_REQUIRED = {'response_code': 1472,
                            'message': 'Please provide a business id document', 'status_code': 400}
    ADDRESS_PROOF_REQUIRED = {'response_code': 1471,
                              'message': 'Please provide an address proof id document', 'status_code': 400}
    ACCOUNT_TYPE_EXIST = {'response_code': 1470,
                          'message': 'An account with given type already exists.', 'status_code': 400}
    INVALID_NIBSS_ACCOUNT = {'response_code': 1469,
                             'message': 'Missing environmental variable ADD_NIBSS_ACCOUNT_QUEUE_NAME',
                             'status_code': 403}
    ACCOUNT_NUMBER_MUST_BE_10 = {'response_code': 1468,
                                 'message': 'Account number must be a 10-digit integer',
                                 'status_code': 400}

    '''
          ERROR TYPE : BILL PAYMENT ERRORS
          CODE : 13
          DESCRIPTION : BILL PAYMENT  ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM & REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    INCORRECT_BILL_CATEGORY = {'response_code': 1399, 'message': 'category must be either send_money or bill',
                               'status_code': 400}
    INCORRECT_BILLER_TYPE = {'response_code': 1398, 'message': 'Incorrect biller type.', 'status_code': 400}
    INVALID_CATEGORY_ID = {'response_code': 1397, 'message': 'Please pass the category id for the bill payment',
                           'status_code': 400}
    INVALID_BILLER_ID = {'response_code': 1396, 'message': 'biller id is required', 'status_code': 400}
    UNABLE_FETCH_BILLERS = {'response_code': 1395, 'message': 'unable to fetch billers', 'status_code': 400}
    FAILED_CUSTOMER_VALIDATION = {'response_code': 1394, 'message': 'failed to validate customer', 'status_code': 400}
    INVALID_BILL_VOUCHER = {'response_code': 1393, 'message': 'Voucher type must be either recharge or gift', 'status_code': 400}
    VOUCH_CODE_NOT_FOUND = {'response_code': 1392, 'message': 'Vouch code does not exist', 'status_code': 404}
    VOUCH_CODE_HAS_BEEN_REDEEMED = {'response_code': 1391, 'message': 'Vouch code has already been redeemed', 'status_code': 400}
    VOUCHER_INITIATOR_HAS_INSUFFICIENT_FUND = {'response_code': 1390, 'message': 'The vouch code owner has insufficient fund', 'status_code': 400}
    UNABLE_TO_CREATE_VOUCHER = {'response_code': 1389, 'message': 'Unable to create voucher at the moment.', 'status_code': 500}
    UNABLE_TO_REDEEM_VOUCHER = {'response_code': 1388, 'message': 'Unable to redeem the voucher at the moment. please retry again',
                                'status_code': 500}
    UNABLE_TO_PROCESS_BILL = {'response_code': 1387, 'message': 'Unable to process the bill at the moment. please retry again', 'status_code': 500}

    '''
          ERROR TYPE : OVERDRAFT ERRORS
          CODE : 12
          DESCRIPTION : OVERDRAFT  ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''
    NOT_3MONTHS_OLD = {'response_code': 1299, 'message': 'User must be a 3kle user for up to 3 months',
                       'status_code': 400}
    OVERDRAFT_EXIST = {'response_code': 1298, 'message': 'You already have an active/processing overdraft',
                       'status_code': 400}
    OVERDRAFT_AMOUNT_EXCEED = {'response_code': 1297, 'message': 'Amount requested is greater than the overdraft offer',
                               'status_code': 400}
    MANDATE_FAILED = {'response_code': 1296, 'message': 'Creating mandate failed', 'status_code': 400}
    MANDATE_DECLINED = {'response_code': 1295, 'message': 'The mandate request from your bank was declined',
                        'status_code': 400}
    NO_OVERDRAFT_FOUND = {'response_code': 1294, 'message': 'User has no Overdraft', 'status_code': 400}
    NO_PROCESSING_OVERDRAFT_FOUND = {'response_code': 1293, 'message': 'User has no processing Overdraft',
                                     'status_code': 400}
    IRREGULAR_INCOME_FLOW = {'response_code': 1292, 'message': 'User does not have regular income',
                             'status_code': 400}

    '''
          ERROR TYPE : BUDGET SPENDING ERRORS
          CODE : 11
          DESCRIPTION : BUDGET SPENDING  ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    BUDGET_NOT_FOUND = {'response_code': 1199, 'message': 'Budget not found', 'status_code': 404}
    CREATE_A_BUDGET = {'response_code': 1198, 'message': 'Please create a budget for the month', 'status_code': 400}
    BUDGET_HAS_NO_BUDGET = {'response_code': 1197, 'message': 'All category must have an item', 'status_code': 400}
    INVALID_BUDGET_AMOUNT = {'response_code': 1196, 'message': 'Invalid Amount. An item has amount as O',
                             'status_code': 400}
    DUPLICATE_BUDGET = {'response_code': 1195, 'message': 'You have a duplicate item inside a category!',
                        'status_code': 400}
    BUDGET_ITEM_HAS_NO_AMOUNT = {'response_code': 1194,
                                 'message': 'Total Amount on each Item does not match it category amount',
                                 'status_code': 400}
    BUDGET_CATEGORY_NOT_FOUND = {'response_code': 1193, 'message': 'Category does not exist', 'status_code': 404}
    ITEM_WITHDRAWN = {'response_code': 1192, 'message': 'You have already withdrawn {attributes}', 'status_code': 400}
    ACTIVE_BUDGET_EXIST = {'response_code': 1191, 'message': 'You have an active budget running', 'status_code': 400}
    INVALID_BUDGET_CATEGORY = {'response_code': 1190,
                               'message': "The category passed doesn't match the category in database",
                               'status_code': 400}
    BUDGET_ITEM_EXIST = {'response_code': 1189, 'message': "Item : {attributes} already exist in the category",
                         'status_code': 400}
    BUDGET_ITEM_NOT_FOUND = {'response_code': 1188, 'message': "Item : {attributes} does not exist in the category",
                             'status_code': 404}
    MISSING_ITEMS = {'response_code': 1187, 'message': "{attributes}", 'status_code': 404}
    WITHDRAWN_ITEM_UNEDITABLE = {'response_code': 1186, 'message': 'Cannot edit an item that has been withdrawn',
                                 'status_code': 400}
    '''
          ERROR TYPE : SPEND SAVE ERRORS
          CODE : 10
          DESCRIPTION : SPEND SAVE  ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    INVALID_CHANNEL = {'response_code': 1099, 'message': "Invalid channel", 'status_code': 404}
    TRANSACTION_NOT_FROM_ACCOUNT = {'response_code': 1098, 'message': "Transaction not from an account",
                                    'status_code': 400}
    SPEND_SAVE_DISABLED = {'response_code': 1097, 'message': "Spend save is disabled.", 'status_code': 400}

    '''
          ERROR TYPE : SPLIT MONEY ERRORS
          CODE : 20
          DESCRIPTION : SPLIT MONEY ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    AMOUNT_DOES_NOT_MATCH = {'response_code': 2099,
                             'message': "Individual Amounts passed does not match with the total amount",
                             'status_code': 400}
    USERS_MSISDN_NOT_3KLE = {'response_code': 2098, 'message': "Please ensure that all users Msisdn are 3kle users",
                             'status_code': 400}
    BILL_NOT_FOUND = {'response_code': 2097, 'message': "Bill not found!", 'status_code': 404}
    CREATOR_UNABLE_TO_PAY = {'response_code': 2096, 'message': "Creator of the split bill can not make payment",
                             'status_code': 400}
    BILL_ALREADY_PAID = {'response_code': 2095, 'message': "Bill has already been paid", 'status_code': 400}
    AMOUNT_GREATER_THAN_ASSIGNED = {'response_code': 2094,
                                    'message': "Amount is greater than the assigned amount to the user",
                                    'status_code': 400}
    CREATOR_CANNOT_REJECT_BILL = {'response_code': 2093, 'message': "Creator of the split bill can not reject a bill",
                                  'status_code': 400}
    BILL_ALREADY_CANCELLED = {'response_code': 2092, 'message': "Bill has already been cancelled", 'status_code': 400}
    ONLY_CREATOR_CAN_DELETE_BILL = {'response_code': 2092, 'message': "Only bill creator can delete the bill",
                                    'status_code': 400}
    '''
          ERROR TYPE : REQUEST MONEY ERRORS
          CODE : 21
          DESCRIPTION : REQUEST MONEY ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    INVALID_MONEY_REQUEST = {'response_code': 2199, 'message': "Money must be requested from other users",
                             'status_code': 400}
    REQUEST_ALREADY_FULFILLED = {'response_code': 2198, 'message': "Request has already been fulfilled",
                                 'status_code': 400}
    REQUEST_ALREADY_REJECTED = {'response_code': 2197, 'message': "Request has already been rejected",
                                'status_code': 400}
    INVALID_REFERENCE_CODE = {'response_code': 2196, 'message': "Invalid reference code",
                              'status_code': 400}
    CANNOT_CLAIM_SELF_MONEY = {'response_code': 2195, 'message': 'Cannot claim self money request', 'status_code': 400}

    '''
          ERROR TYPE : QUICK LOAN ERRORS
          CODE : 22
          DESCRIPTION : QUICK LOAN ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    NO_QUICK_LOAN_IDENTITY = {'response_code': 2299, 'message': 'User has no identity for this loan',
                              'status_code': 404}
    BANNED_FROM_QUICK_LOAN = {'response_code': 2298, 'message': 'User has already been banned from accessing this loan',
                              'status_code': 400}
    USER_ALREADY_HAS_ACCESS_TO_LOAN = {'response_code': 2297, 'message': 'User has already has access to this loan',
                                       'status_code': 400}
    USER_IDENTITY_ROW_NOT_FOUND = {'response_code': 2296, 'message': 'User Identity Row does not exist',
                                   'status_code': 404}
    STILL_VERIFYING_BUSINESS = {'response_code': 2295, 'message': 'We are still verifying your Business information',
                                'status_code': 400}
    INVALID_PAYLOAD = {'response_code': 2294, 'message': 'Invalid Payload', 'status_code': 400}
    LOW_CREDIT_SCORE = {'response_code': 2293, 'message': 'Your credit score is  low to get a loan',
                        'status_code': 400}
    NO_PROCESSING_LOAN = {'response_code': 2292, 'message': 'User has no processing loan', 'status_code': 400}
    NO_CREDIT_SCORE = {'response_code': 2291, 'message': 'User has no credit score', 'status_code': 400}
    MUST_BE_EMPLOYED = {'response_code': 2290,
                        'message': 'You must be employed before you can be eligible to get a loan', 'status_code': 400}
    NO_ACTIVE_LOAN = {'response_code': 2289, 'message': 'You have no active loan', 'status_code': 404}
    NO_DUE_LOAN = {'response_code': 2288, 'message': 'You have no due loan at the moment.', 'status_code': 400}
    AMOUNT_MUST_EQUAL_LOAN_BALANCE = {'response_code': 2287,
                                      'message': 'The amount must be equal to the total due loan balance',
                                      'status_code': 400}
    COMPLETE_LOAN_PAYMENT_REQUIRED = {'response_code': 2286,
                                      'message': 'Please you are required to make complete payment for the last the loan plan',
                                      'status_code': 400}
    LOAN_EXTENSION_REACHED = {'response_code': 2285, 'message': 'You have reached your limit on loan extension',
                              'status_code': 400}
    STILL_VERIFYING_PERSONAL = {'response_code': 2284, 'message': 'We are still verifying your personal information',
                                'status_code': 400}
    LOAN_NOT_FOUND = {'response_code': 2283, 'message': 'Loan does not exist', 'status_code': 404}
    NO_APPROVED_LOAN = {'response_code': 2282, 'message': 'You have no approved loan', 'status_code': 400}
    AMOUNT_MUST_WITHIN_LOAN_BALANCE = {'response_code': 2281,
                                       'message': 'Amount to pay is greater than the loan balance',
                                       'status_code': 400}

    '''
          ERROR TYPE : PEER TO PEER LOANS ERRORS
          CODE : 23
          DESCRIPTION : PEER TO PEER LOANS ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''

    AUTO_LOAN_NOT_FOUND = {'response_code': 2399, 'message': 'Auto loan not found', 'status_code': 404}
    INCOMPLETE_PROFILE = {'response_code': 2398, 'message': 'We noticed your profile is incomplete', 'status_code': 400}
    ACTIVE_LOAN_EXIST = {'response_code': 2397, 'message': 'Loan not created, You currently have an active loan',
                         'status_code': 400}
    PENDING_LOAN_EXIST = {'response_code': 2396, 'message': 'Loan not created, You currently have an pending loan',
                          'status_code': 400}
    PAYBACK_MUST_BE_LESS_THAN_12_MONTHS = {'response_code': 2395,
                                           'message': 'Payback period cannot be greater than 12 months',
                                           'status_code': 400}
    INTEREST_RATE_MUST_BE_6_TO_12 = {'response_code': 2394,
                                     'message': 'Interest rate must fall between 6 to 20 percent inclusive',
                                     'status_code': 400}
    LOAN_CANNOT_BE_SPONSORED = {'response_code': 2393, 'message': 'Loan cannot be sponsored', 'status_code': 400}
    YOU_CANNOT_SPONSOR_SELF_LOAN = {'response_code': 2392, 'message': 'You cannot sponsor your own loan.',
                                    'status_code': 400}
    SPONSORSHIP_ALREADY_EXIST = {'response_code': 2391, 'message': 'Sponsorship request already exists',
                                 'status_code': 400}
    SPONSORSHIP_HAS_EXPIRED = {'response_code': 2390, 'message': 'Sponsorship request has expired', 'status_code': 400}
    SPONSOR_HAS_INSUFFICIENT_LOAN = {'response_code': 2389,
                                     'message': 'Operation failed, sponsor has insufficient balance',
                                     'status_code': 400}
    TAKE_ELIGIBILITY_TEST = {'response_code': 2388, 'message': 'Please take a loan eligibility test',
                             'status_code': 400}
    ELIGIBLE_FOR_25000 = {
        'response_code': 2387,
        'message': 'You are eligible for up to 25,000 at this time. The more you borrow and payback on time, you will be able to borrow more',
        'status_code': 400
    }

    UNABLE_TO_PERFORM_ELIGIBILITY_CHECK = {'response_code': 2386,
                                           'message': 'Cannot perform an eligibility check at this time',
                                           'status_code': 400}
    LOAN_MUST_BE_ACTIVE = {'response_code': 2385, 'message': 'Loan must be active.', 'status_code': 400}
    MANDATE_NOT_APPROVED = {'response_code': 2384,
                            'message': "Mandate for this loan has not been approved, payback cannot be made for a loan that hasn\'t been received",
                            'status_code': 400}
    LOAN_NOT_INSTALLMENT = {'response_code': 2383, 'message': "This loan is not an installment payment type",
                            'status_code': 400}
    PAYMENT_FAILED = {'response_code': 2383, 'message': "Payment failed", 'status_code': 500}
    SUPPLIED_ID_NOT_FOUND = {'response_code': 2382, 'message': "No autoloan matched the supplied id",
                             'status_code': 404}
    ONLY_LENDER_CAN_SEND_REQUEST = {'response_code': 2381, 'message': "Only lender can send payment request",
                                    'status_code': 400}
    PAYMENT_NOT_DUE = {'response_code': 2380, 'message': "Payment is not due today for this loan", 'status_code': 400}
    PAYMENT_ALREADY_MADE = {'response_code': 2379, 'message': "Payment has already been made", 'status_code': 400}
    MANDATE_ALREADY_APPROVED = {'response_code': 2378, 'message': "Mandate has been approved for this loan already",
                                'status_code': 400}
    LOAN_ALREADY_COMPLETED = {'response_code': 2377, 'message': 'Invalid request, this loan has been completed',
                              'status_code': 400}
    LOAN_AMOUNT_MUST_BE_POSITIVE_NUMBER = {'response_code': 2376, 'message': 'Loan amount must be non-negative number',
                                           'status_code': 400}
    INVALID_PAYBACK_PERIOD = {'response_code': 2375, 'message': 'Invalid value for payback period', 'status_code': 400}
    LOAN_TIP_MUST_BE_NUMBER = {'response_code': 2374, 'message': 'Loan tip amount must be a number', 'status_code': 400}
    INTEREST_RATE_MUST_BE_NUMBER = {'response_code': 2373, 'message': 'Interest rate amount must be a number',
                                    'status_code': 400}
    BUSINESS_REVENUE_MUST_BE_POSITIVE_NUMBER = {'response_code': 2372,
                                                'message': 'Business yearly revenue must be non-negative number',
                                                'status_code': 400}
    UNABLE_TO_BORROW_AT_THE_MOMENT = {'response_code': 2371,
                                      'message': 'Apologies, but you are not eligible to borrow a loan at this time',
                                      'status_code': 400}
    INELIGIBLE_FOR_A_LOAN = {'response_code': 2370, 'message': "You\'re not eligible for a loan", 'status_code': 400}
    CREDIT_SCORE_SERVICE_FAILED = {'response_code': 2369, 'message': "Credit score service failed", 'status_code': 400}
    CREDIT_SCORE_SERVICE_UNAVAILABLE = {'response_code': 2368, 'message': "Could not connect to credit score service",
                                        'status_code': 503}
    PAYBACK_MAX_4_WEEKS = {'response_code': 2367, 'message': "Payback period cannot be greater than 4 weeks",
                           'status_code': 400}
    NEW_USER_ELIGIBLE_FOR_25000 = {'response_code': 2366,
                                   'message': "As a new user, you are eligible for up to 25,000 at this time",
                                   'status_code': 400}
    ELIGIBLE_FOR_30000 = {'response_code': 2365, 'message': "You are eligible for up to 30,000 at this time",
                          'status_code': 400}
    LENDER_WALLET_NOT_FOUND = {'response_code': 2364, 'message': "Lender wallet not found", 'status_code': 404}
    MANDATE_UNAVAILABLE = {'response_code': 2363, 'message': "Could not connect to nibss mandate service",
                           'status_code': 503}
    BANK_ERROR_OCCURRED = {'response_code': 2362,
                           'message': "An error has occurred, please review your bank details and try again",
                           'status_code': 400}
    UNABLE_TO_CREATE_MANDATE = {'response_code': 2361, 'message': "Mandate could not be created", 'status_code': 504}
    TIN_VERIFICATION_FAILED = {'response_code': 2360, 'message': "TIN verification failed", 'status_code': 400}

    '''
          ERROR TYPE : NQR ERRORS
          CODE : 24
          DESCRIPTION : NQR ERROR USED ON THE SYSTEM.
          ADD NEW ERRORS FROM BOTTOM AND REMEMBER TO FOLLOW THE RESPONSE CODE NUMBER PATTERN
      '''
    INVALID_DESTINATION_TYPE = {'response_code': 2499, 'message': "Invalid destination type must be either (personal or business)", 'status_code': 400}
    AMOUNT_NEEDED_FOR_DYNAMIC_QR = {'response_code': 2498, 'message': "Amount is needed for dynamic QR code creation", 'status_code': 400}
