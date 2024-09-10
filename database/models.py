import uuid

from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column

from utils.utils import get_current_time
from utils.enums.user_status import UserStatus
from database.create import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger, unique=True)
    status: Mapped[UserStatus] = mapped_column(ENUM(UserStatus, name="user_status"), default=UserStatus.user)
    created_at: Mapped[str] = mapped_column(default=get_current_time)