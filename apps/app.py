from config.star_filter_config import *
from models.college_info_model import *


@app.route('/get_all', methods=['GET'])
def home():
    """star filter condition """
    filter1 = []
    try:
        if request.args.get("studentname"):
            filter1.append(CollegeInfo.studentName == request.args.get("studentname"))
        if request.args.get("fathername"):
            filter1.append(CollegeInfo.fatherName == request.args.get("fathername"))
        if request.args.get("mothename"):
            filter1.append(CollegeInfo.motherName == request.args.get("mothename"))
        if request.args.get("stream"):
            filter1.append(CollegeInfo.stream == request.args.get("stream"))
        if request.args.get("dob"):
            filter1.append(CollegeInfo.dob == request.args.get("dob"))
        if request.args.get("state"):
            filter1.append(CollegeInfo.state == request.args.get("state"))
        result = session.query(CollegeInfo).filter(*filter1).all()
        result = [i.__dict__ for i in result]
    except Exception as err:
        log.debug ("error is ",err)
        session.rollback()
    finally:
        session.close()
        return str(result)

app.run(debug=False)
