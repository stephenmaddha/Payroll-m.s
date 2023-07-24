import sqlite3

class Employee:
    def empinsert(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' INSERT INTO EMPLOYEE_DETAILS
                    VALUES({k['eid']},"{k['ename']}",{k['dptid']},
                    "{k['designation']}","{k['email']}",{k['contact']},
                    "{k['address']}")
            ''')
        conn.commit()
    
    def show_employees(self):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM EMPLOYEE_DETAILS")
        data = []

        for i in cur.fetchall():
            context = {}
            context['eid'] = i[0]
            context['ename'] = i[1]
            context['dptid'] = i[2]
            context['designation'] = i[3]
            context['email'] = i[4]
            context['contact'] = i[5]
            context['address'] = i[6]
            data.append(context)
        return data
    def attendance(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' INSERT INTO attedance
                    VALUES({k['dptid']},"{k['dptname']}",{k['eid']},
                    "{k['ename']}","{k['date']}","{k['timein']}",
                    "{k['timeout']}")
            ''')
        conn.commit()

    def salaryinsert(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' INSERT INTO SALLARY_DETAILS
                    VALUES({k['eid']},{k['dptid']},
                    {k['account_number']},"{k['pan']}",{k['base_sallary']})
            ''')
        conn.commit()
    
class salarycalcuator:
    def salarycalucation(self,eid):
        Conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f"SELECT BASE_SALARY FROM SALLARY_DETAILS WHERE EID={eid}")
        bs=cur.fetchall()[0][0]
        cur.execute(f"SELECT DATE,TIMEOUT,TIMEIN FROM ATTEDANCE WHERE EID={eid}")
        gt=cur.fetchall()
        print(bs)
        print(gt)
        hrs=bs/(22*8)
        su=0
        for i in gt:
            g=int((i[2][:2])-(i[1][:2]))*hrs
            su=su+g
        return su
    