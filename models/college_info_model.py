from config.star_filter_config import *


class CollegeInfo(Base):
    __tablename__ = "collegeinfo"
    studentName = Column("student_name",String)
    fatherName = Column("father_name", String)
    motherName = Column ("mother_name",String)
    stream = Column("stream", String)
    dob = Column("dob", Date)
    state = Column("state",String)
    gender = Column("gender", String)
    mob = Column("mob", Integer, primary_key=True)
    marks = Column("marks", Integer)
    country = Column("country", String)
    joiningDate = Column("joining_date", Date)

