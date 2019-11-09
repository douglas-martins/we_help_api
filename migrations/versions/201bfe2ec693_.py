"""empty message

Revision ID: 201bfe2ec693
Revises: 
Create Date: 2019-11-09 10:42:30.719798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '201bfe2ec693'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    op.drop_table('welcoming')
    op.drop_table('welcoming_available')
    op.drop_table('chat_history')
    op.drop_table('aid_institution')
    op.drop_table('chat_room')
    op.drop_table('chat_history_media')
    op.drop_table('user_anonymous')
    op.drop_table('file')
    op.alter_column('contact', 'created_at',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contact', 'created_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.create_table('file',
    sa.Column('id', sa.INTEGER(), server_default=sa.text(u"nextval('file_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'file_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('user_anonymous',
    sa.Column('id', sa.INTEGER(), server_default=sa.text(u"nextval('user_anonymous_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.CHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_anonymous_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('chat_history_media',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('chat_history_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('deleted_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], [u'chat_history.id'], name=u'chat_history_fkey'),
    sa.ForeignKeyConstraint(['id'], [u'file.id'], name=u'file_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'chat_history_media_pkey')
    )
    op.create_table('chat_room',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('welcoming_available_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_anonymous_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('chat_history_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], [u'user_anonymous.id'], name=u'user_anonymous_fkey'),
    sa.ForeignKeyConstraint(['id'], [u'welcoming_available.id'], name=u'welcoming_available_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'chat_room_pkey')
    )
    op.create_table('aid_institution',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('contact_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('url_site', sa.CHAR(length=500), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], [u'contact.id'], name=u'contact_fkey'),
    sa.ForeignKeyConstraint(['id'], [u'file.id'], name=u'file_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'aid_institution_pkey')
    )
    op.create_table('chat_history',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('welcoming_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_anonymous_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('deleted_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], [u'user_anonymous.id'], name=u'user_anonymous_fkey'),
    sa.ForeignKeyConstraint(['id'], [u'welcoming.id'], name=u'welcoming_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'chat_history_pkey')
    )
    op.create_table('welcoming_available',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('welcoming_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('on_chat', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], [u'welcoming.id'], name=u'welcoming_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'welcoming_available_pkey')
    )
    op.create_table('welcoming',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('person_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('updated_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], [u'person.id'], name=u'person_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'welcoming_pkey')
    )
    op.create_table('person',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('contact_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.CHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('deleted_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('updated_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], [u'contact.id'], name=u'contact_fkey'),
    sa.ForeignKeyConstraint(['id'], [u'file.id'], name=u'file_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'person_pkey')
    )
    # ### end Alembic commands ###
