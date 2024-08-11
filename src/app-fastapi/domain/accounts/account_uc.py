
class AccountUseCase:
    
    def __init__(self, repo: IrepAccount) -> None:
        self._repo = repo

    def get_all_accounts(self):