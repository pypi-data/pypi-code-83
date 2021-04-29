from curriculum_model.db import DB
from curriculum_model.db.schema import Curriculum
import sys

if getattr(sys, 'frozen', False) or __name__ == "__main__":
    print("Curriculum Model")
    with DB() as db:
        s = db.session()
        print(s.query(Curriculum).all())
