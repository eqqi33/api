"""
    cloudplayer.api.model.account
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by the cloudplayer team
    :license: GPL-3.0, see LICENSE for details
"""
from sqlalchemy.sql import func
import sqlalchemy as sql
import sqlalchemy.orm as orm

from cloudplayer.api.model import Base


class Account(Base):

    __tablename__ = 'account'
    __fields__ = [
        'id',
        'provider_id',
        'user_id',
        'created',
        'updated',
        'title',
        'image'
    ]
    __filters__ = [
        'provider_id',
        'title'
    ]
    __mutable__ = [
        'title',
        'image'
    ]
    __public__ = [
        'id',
        'provider_id',
        'title',
        'image'
    ]
    __table_args__ = (
        sql.PrimaryKeyConstraint(
            'id', 'provider_id'),
        sql.ForeignKeyConstraint(
            ['provider_id'],
            ['provider.id']),
        sql.ForeignKeyConstraint(
            ['user_id'],
            ['user.id']),
        sql.ForeignKeyConstraint(
            ['image_id'],
            ['image.id']),
    )

    id = sql.Column(sql.String(32))

    account_id = orm.synonym('id')

    provider_id = sql.Column(sql.String(16))
    provider = orm.relationship('Provider')

    user_id = sql.Column(sql.Integer, nullable=False)
    user = orm.relationship('User', back_populates='accounts')

    playlists = orm.relationship('Playlist', back_populates='account')

    tracks = orm.relationship('Track', back_populates='account')

    title = sql.Column('title', sql.String(64))
    image_id = sql.Column(sql.Integer)
    image = orm.relationship('Image')

    created = sql.Column(
        sql.DateTime(timezone=True), server_default=func.now())
    updated = sql.Column(
        sql.DateTime(timezone=True), server_default=func.now(),
        onupdate=func.now())

    access_token = sql.Column(sql.String(256))
    refresh_token = sql.Column(sql.String(256))
    token_expiration = sql.Column(sql.DateTime(timezone=True))