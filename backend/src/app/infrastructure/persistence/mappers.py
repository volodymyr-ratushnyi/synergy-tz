from app.domain.entities.post import Post
from app.domain.entities.user import User
from app.infrastructure.persistence.models.post_model import PostModel
from app.infrastructure.persistence.models.user_model import UserModel


def to_user_entity(model: UserModel) -> User:
    return User(
        external_id=model.external_id,
        first_name=model.first_name,
        last_name=model.last_name,
        email=model.email,
        username=model.username,
        image=model.image,
        role=model.role,
    )


def to_post_entity(model: PostModel) -> Post:
    return Post(
        external_id=model.external_id,
        user_external_id=model.user_external_id,
        title=model.title,
        body=model.body,
        views=model.views,
        tags=model.tags,
        reactions=model.reactions,
    )
