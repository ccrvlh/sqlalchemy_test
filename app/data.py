# Module
from .models import AccountClassification, AccountSubType, AccountType

# AccountsClassification
assets = AccountClassification(classification="assets")
liabilities = AccountClassification(classification="liabilities")

# Types
current_assets = AccountType(title="current assets")
non_current_assets = AccountType(title="non-current assets")
current_liabilities = AccountType(title="current liabilities")
non_current_liabilities = AccountType(title="non-current liabilities")
equity = AccountType(title="equity")

# Subtypes
cash = AccountSubType(subtype="cash & equivalents")
receivables = AccountSubType(subtype="accounts receivable")
other_current_assets = AccountSubType(subtype="other current assets")
investments_lt = AccountSubType(subtype="long term investments")
ppe = AccountSubType(subtype="property, plant & equipment")
accounts_payable = AccountSubType(subtype="accounts payable")
payroll_payabale = AccountSubType(subtype="payroll payable")
st_debt = AccountSubType(subtype="short term debt")
lt_debt = AccountSubType(subtype="long term debt")
shareholders_equity = AccountSubType(subtype="shareholders equity")

# Relations
assets.children.append(current_assets)
assets.children.append(non_current_assets)
liabilities.children.append(current_liabilities)
liabilities.children.append(non_current_liabilities)
current_assets.children.append(cash)
current_assets.children.append(receivables)
non_current_assets.children.append(ppe)
non_current_assets.children.append(investments_lt)
current_liabilities.children.append(accounts_payable)
current_liabilities.children.append(st_debt)
non_current_liabilities.children.append(lt_debt)
equity.children.append(shareholders_equity)

system_accounts = [
    assets,
    liabilities,
    equity,
    current_assets,
    non_current_assets,
    current_liabilities,
    non_current_liabilities
]
