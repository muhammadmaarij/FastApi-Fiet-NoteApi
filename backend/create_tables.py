from backend.models.models import Base  # Use absolute import
from backend.db.database import engine  # Use absolute import


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
