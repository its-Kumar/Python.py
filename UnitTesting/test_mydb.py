import pytest
from mydb import MyDB

# conn = None
# cur = None


# dependency injuction
@pytest.fixture(scope="module")
def cur():
    print("Setting up.....")
    db = MyDB()
    conn = db.connect("server")
    cur_ = conn.cursor()
    yield cur_
    cur_.close()
    conn.close()
    print("closing database....")


"""
def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()


def teardown_module(module):
    cur.close()
    conn.close()
"""


def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123


def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789


# `pytest --capture=no`
