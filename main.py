class From_wallet:
    def __init__(self, hash_from: str) -> None:
        self.hash_from: str = hash_from


class To_wallet:
    def __init__(self, hash_to: str) -> None:
        self.hash_to: str = hash_to


class Value:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount


class Seed:
    def __init__(self, seed: str) -> None:
        self.seed: str = seed


class Transaction:
    def __init__(
        self, From: From_wallet, To: To_wallet, seed: Seed, value: Value
    ) -> None:
        self.From: From_wallet = From
        self.To: To_wallet = To
        self.seed: Seed = seed
        self.value: Value = value


class Block_chain:
    def __init__(self, transaction: Transaction) -> None:
        self.transaction: Transaction = transaction

    def Generate_proof(self) -> str:
        if self.transaction != None and self.transaction.seed == "SHA256":
            return print("success")
        else:
            return print("error")


# solana = Transaction("VASYL", "KATE", "SHA256", 10)
web_request = Block_chain(Transaction("VASYL", "KATE", "ed25519", 10)).Generate_proof()
# web_request.Generate_proof()
