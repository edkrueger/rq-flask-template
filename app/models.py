"""SQLAlchemy database models."""
import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import JSON, DateTime

from .database import Base


class DictMixIn:
    """Provides a to_dict method to a SQLAlchemy database model."""

    def to_dict(self):
        """Returns a JSON serializable dictionary from a SQLAlchemy database model."""
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }


class Result(Base, DictMixIn):
    """A SQLAlchemy model for the Results table."""

    __tablename__ = "Results"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String(36), index=True)
    job_enqueued_at = Column(DateTime)
    job_started_at = Column(DateTime)
    input = Column(JSON)
    result = Column(JSON)
