from datetime import datetime, timedelta

from app import TimelinePost


def test_create_timeline_post_sets_fields():
    post = TimelinePost.create(name="Ada", email="ada@example.com", content="Hello world")

    assert post.id is not None
    assert post.name == "Ada"
    assert post.email == "ada@example.com"
    assert post.content == "Hello world"
    assert isinstance(post.created_at, datetime)


def test_select_returns_empty_when_no_posts_exist():
    assert list(TimelinePost.select()) == []


def test_posts_ordered_by_created_at_desc():
    older = TimelinePost.create(
        name="Ada",
        email="ada@example.com",
        content="First",
        created_at=datetime.now() - timedelta(minutes=5),
    )
    newer = TimelinePost.create(name="Grace", email="grace@example.com", content="Second")

    posts = list(TimelinePost.select().order_by(TimelinePost.created_at.desc()))

    assert [p.id for p in posts] == [newer.id, older.id]


def test_get_by_id_returns_matching_post():
    post = TimelinePost.create(name="Ada", email="ada@example.com", content="Hello world")

    fetched = TimelinePost.get_by_id(post.id)

    assert fetched.name == "Ada"
    assert fetched.content == "Hello world"
