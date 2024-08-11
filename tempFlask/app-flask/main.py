from flask import Flask
from .domain import (
    get_all_accounts,
    get_account_by_id,
    create_account,
    put_account,
    patch_account,
    delete_account,
)

app = Flask(__name__)

app.add_url_rule("/api/v1/accounts/", endpoint="get_all_accounts", view_func=get_all_accounts, methods=["GET"])
app.add_url_rule("/api/v1/accounts/<uuid:uid>", endpoint="get_account_by_id", view_func=get_account_by_id, methods=["GET"])
app.add_url_rule("/api/v1/accounts/", endpoint="create_account", view_func=create_account, methods=["POST"])
app.add_url_rule("/api/v1/accounts/<uuid:uid>", endpoint="put_account", view_func=put_account, methods=["PUT"])
app.add_url_rule("/api/v1/accounts/<uuid:uid>", endpoint="patch_account", view_func=patch_account, methods=["PATCH"])
app.add_url_rule("/api/v1/accounts/<uuid:uid>", endpoint="delete_account", view_func=delete_account, methods=["DELETE"])
