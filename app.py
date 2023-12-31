from flask import Flask, render_template,jsonify,request
from employee import Employee,salarycalcuator
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee/signup', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        eid = request.form.get('eid')
        ename = request.form.get('ename')
        dptid = request.form.get('dptid')
        designation = request.form.get('designation')
        email = request.form.get('email')
        contact = request.form.get('contact')
        address = request.form.get('address')
        print(eid,ename,dptid)
        emp = Employee()
        emp.empinsert(eid = eid,ename=ename,dptid = dptid,designation=designation,email=email,contact=contact,address=address)
        return render_template('message.html')
    else:
        return render_template('signup.html')

@app.route('/employees',methods = ['GET','POST'])
def show_employees():
    emp = Employee()
    data = emp.show_employees()
    return render_template('showemployees.html',employees = data)

@app.route('/attendance',methods = ['GET','POST'])
def attendance():
    if request.method=='POST':
        dptid = request.form.get("dptid")
        dptname = request.form.get("dptname")
        eid= request.form.get("eid")
        ename= request.form.get("ename")
        date= request.form.get("date")
        timein= request.form.get("timein")
        timeout= request.form.get("timeout")

        emp = Employee()
        emp.attendance(dptid = dptid,dptname = dptname,eid = eid,ename = ename,date = date,timein = timein,timeout = timeout)
        return render_template('message.html')
    else:
        return render_template('attedance.html')

@app.route('/salary/details',methods=['GET','POST'])
def salarydetails():
    if request.method=='POST':
        eid=request.form.get("eid")
        dptid=request.form.get("dptid")
        acc_no=request.form.get("account_number")
        pan=request.form.get("pan")
        bs=request.form.get("base_salary")
        emp=Employee()
        emp.salaryinsert(eid=eid,dptid=dptid,account_number=acc_no,pan=pan,base_sallary=bs)
        return render_template('message.html')
    else:
        return render_template('salarydetails.html')
    
@app.route('/payroll/release',methods=['GET','POST'])
def payrollrelease():
    if request.method=='POST':
        eid=request.form.get("empid")
        sc=salarycalcuator
        total_salary=sc.salarycalucation(eid=int(eid))
        context={'EmoplyeeID':eid,'TotalSalary':int(total_salary)}
        return render_template('showsalary.html',data=context)
    else:
        return render_template('empid.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)