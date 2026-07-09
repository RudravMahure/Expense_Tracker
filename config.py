from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

MONTHLY_BUDGET_FILE = DATA_DIR / "monthly_budget.txt"
ADD_EXPENSE_FILE = DATA_DIR / "sample_expenses.txt"