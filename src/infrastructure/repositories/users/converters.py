from src.domain.users.entity import User


def convert_user_entity_to_document(user: User) -> dict:
    return {
        "oid": user.oid,
        "email": user.email,
    }
