import sqlalchemy as sa
from db import Base
from datetime import datetime

class Blog(Base):
    __tablename__ = "blogs"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    created_by = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now())
    updated_at = sa.Column(sa.DateTime, default=datetime.now())
    deleted_at = sa.Column(sa.DateTime, nullable=True, default=None)

# PSQL create table query
"""
CREATE TABLE blogs (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description TEXT NOT NULL,
    created_by VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL DEFAULT NULL
);
"""
