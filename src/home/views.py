from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from src.home.models import Students
from src.home.models import Courses
from src.home.models import Semester
from src.home.models import Update
import hashlib
import json
from cryptography.fernet import Fernet

key = b'SVxo6F83ZykoPetuVRswTOoaP-TxY2r-6AQyiX7gveg='
f = Fernet(key)


def student(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            # # # --------------------PASS SYSTEM--------------------
            # cc = json.loads(str(stu.CurrentCourses).replace("\'", "\""))
            # uc = json.loads(str(stu.UndergraduateCourses).replace("\'", "\""))
            # pc = json.loads(str(stu.PassedCourses).replace("\'", "\""))
            #
            # for i in range(len(cc)):
            #     if cc[i]["FinalPoint"] >= 3:
            #         pc.append(cc[i])
            #     else:
            #         uc.append(cc[i])
            #
            # cc.clear()
            #
            # stu.CurrentCourses = json.dumps(cc)
            # stu.UndergraduateCourses = json.dumps(uc)
            # stu.PassedCourses = json.dumps(pc)
            #
            # Students.objects.filter(
            #     Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8',
            #                                  100000)).update(CurrentCourses=stu.CurrentCourses,
            #                                                  UndergraduateCourses=stu.UndergraduateCourses,
            #                                                  PassedCourses=stu.PassedCourses)
            # # # ---------------------------------------------------
            # # # ---------------------UPDATE UC---------------------
            # c = Update.objects.get(_id=0)
            # cl = json.loads(str(c.update).replace("\'", "\""))
            # uc = json.loads(str(stu.UndergraduateCourses).replace("\'", "\""))
            # ucid = []
            #
            # for i in range(len(uc)):
            #     ucid.append(str(uc[i]["id"]))
            #
            # for i in range(len(cl)):
            #     if cl[i]["id"] in ucid:
            #         for j in range(len(uc)):
            #             if uc[j]["id"] == cl[i]["id"]:
            #                 uc[j] = cl[i]
            #             else:
            #                 pass
            #     else:
            #         uc.append(cl[i])
            #
            # stu.UndergraduateCourses = json.dumps(uc)
            #
            # Students.objects.filter(
            #     Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8',
            #                                  100000)).update(UndergraduateCourses=stu.UndergraduateCourses)
            # # # ---------------------------------------------------

            return render(request, "home/studentpage.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def profile(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            return render(request, "home/profile.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password"),
                           'SSN': f.decrypt(stu.SSN).decode(),
                           'debit': f.decrypt(stu.DebitCardNumber).decode()})

    if request.method == 'GET':
        return render(request, "homepage.html")


def courses(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            ucl = json.loads(str(stu.UndergraduateCourses).replace("\'", "\""))
            cc = json.loads(str(stu.CurrentCourses).replace("\'", "\""))
            ccl = []
            for i in range(len(cc)):
                ccl.append(str(cc[i]["Course"]))
            pc = json.loads(str(stu.PassedCourses).replace("\'", "\""))
            pcl = []
            for i in range(len(pc)):
                pcl.append(str(pc[i]["Course"]))
            lts = []
            for i in range(len(ucl)):
                if ucl[i]["Course"] in lts:
                    pass
                else:
                    if ucl[i]["Course"] in pcl:
                        pass
                    elif ucl[i]["Course"] in ccl:
                        pass
                    else:
                        lts.append(str(ucl[i]["Course"]))

            return render(request, "home/courses.html",
                          {'student': stu, 'undergraduate': lts,
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def selection(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            return render(request, "home/selection.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def edit(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            return render(request, "home/Edit.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def modify(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            stu.FirstName = str(request.POST.get("first")).title()
            stu.LastName = str(request.POST.get("last")).title()
            stu.DateOfBirth = str(request.POST.get("dob"))
            stu.SSN = f.encrypt(str(request.POST.get("ssn")).encode())
            stu.Password = hashlib.pbkdf2_hmac('sha256', str(request.POST.get("ssn")).encode(), b'2S1A3L7T8',
                                               100000)
            stu.FatherName = str(request.POST.get("father")).title()
            stu.CellularPhoneNumber = request.POST.get("spn")
            stu.FatherCellularPhoneNumber = request.POST.get("fpn")
            stu.MotherCellularPhoneNumber = request.POST.get("mpn")
            stu.Address = request.POST.get("address")
            stu.DebitCardNumber = hashlib.pbkdf2_hmac('sha256', str(request.POST.get("dcn")).encode(), b'2S1A3L7T8',
                                                      100000)
            stu.Email = request.POST.get("email")
            Students.objects.filter(
                Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8',
                                             100000)).update(FirstName=stu.FirstName,
                                                             LastName=stu.LastName,
                                                             DateOfBirth=stu.DateOfBirth,
                                                             SSN=stu.SSN,
                                                             FatherName=stu.FatherName,
                                                             CellularPhoneNumber=stu.CellularPhoneNumber,
                                                             FatherCellularPhoneNumber=stu.FatherCellularPhoneNumber,
                                                             MotherCellularPhoneNumber=stu.MotherCellularPhoneNumber,
                                                             Address=stu.Address,
                                                             DebitCardNumber=stu.DebitCardNumber,
                                                             Password=stu.Password,
                                                             Email=stu.Email)
            return render(request, "home/Edit.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def select(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            cdata = list(json.loads(str(stu.CurrentCourses).replace("\'", "\"")))
            udata = list(json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")))
            clist = Courses.objects.get(id=request.POST.get("code"))
            length = len(udata)
            if len(cdata) == 8:
                return render(request, "home/selection.html",
                              {'student': stu,
                               "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                               "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                               "passed": json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                               'username': request.POST.get("username"), 'password': request.POST.get("password")})
            else:
                i = 0
                while i < length - 1:
                    if udata[i]["Course"] == clist.Course:
                        if udata[i]["id"] == clist.id:
                            cdata.append(udata[i])
                            del udata[i]
                            length -= 1
                        else:
                            i += 1
                    else:
                        i += 1

                stu.CurrentCourses = json.dumps(cdata)
                stu.UndergraduateCourses = json.dumps(udata)
                Students.objects.filter(
                    Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8',
                                                 100000)).update(CurrentCourses=stu.CurrentCourses,
                                                                 UndergraduateCourses=stu.UndergraduateCourses)
                return render(request, "home/selection.html",
                              {'student': stu,
                               'undergraduate': json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                               'current': json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                               'passed': json.loads(str(stu.PassedCourses).replace("\'", "\"")),
                               'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def drop(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            return render(request, "home/drop.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def remove(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):

            cc = list(json.loads(str(stu.CurrentCourses).replace("\'", "\"")))
            uc = list(json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")))
            for i in range(len(cc)):
                if cc[i]["id"] == int(request.POST.get("code")):
                    uc.append(cc[i])
                    del cc[i]

            stu.CurrentCourses = json.dumps(cc)
            stu.UndergraduateCourses = json.dumps(uc)
            Students.objects.filter(
                Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8',
                                             100000)).update(CurrentCourses=stu.CurrentCourses,
                                                             UndergraduateCourses=stu.UndergraduateCourses)

            return render(request, "home/drop.html",
                          {'student': stu,
                           "undergraduate": json.loads(str(stu.UndergraduateCourses).replace("\'", "\"")),
                           "current": json.loads(str(stu.CurrentCourses).replace("\'", "\"")),
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def logout(request):
    if request.method == "POST":
        return render(request, "homepage.html")

    if request.method == 'GET':
        return render(request, "homepage.html")


def point(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            return render(request, "home/point.html",
                          {'student': stu,
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def calculate(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):

            report = Semester.objects.get(_id=stu.id)
            sem = json.loads(str(report.semester1).replace("\'", "\""))

            for i in range(8):
                if str(request.POST.get("semester")) == "semester1":
                    sem = json.loads(str(report.semester1).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester2":
                    sem = json.loads(str(report.semester2).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester3":
                    sem = json.loads(str(report.semester3).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester4":
                    sem = json.loads(str(report.semester4).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester5":
                    sem = json.loads(str(report.semester5).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester6":
                    sem = json.loads(str(report.semester6).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester7":
                    sem = json.loads(str(report.semester7).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester8":
                    sem = json.loads(str(report.semester8).replace("\'", "\""))

            counter = 0
            sop = 0

            for i in range(len(sem)):
                sop += int(sem[i]["FinalPoint"])
                counter += 1

            if int(counter) == 0:
                gpa = ""
            else:
                gpa = float(sop) / int(counter)

            return render(request, "home/point.html",
                          {'student': stu, 'semester': sem, 'GPA': gpa,
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def tuition(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):
            return render(request, "home/tuition.html",
                          {'student': stu,
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")


def payment(request):
    if request.method == 'POST':
        stu = Students.objects.get(
            Username=hashlib.pbkdf2_hmac('sha256', str(request.POST.get("username")).encode(), b'2S1A3L7T8', 100000))
        if stu.Password == hashlib.pbkdf2_hmac('sha256', str(request.POST.get("password")).encode(), b'2S1A3L7T8',
                                               100000):

            report = Semester.objects.get(_id=stu.id)
            sem = json.loads(str(report.semester1).replace("\'", "\""))

            for i in range(8):
                if str(request.POST.get("semester")) == "semester1":
                    sem = json.loads(str(report.semester1).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester2":
                    sem = json.loads(str(report.semester2).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester3":
                    sem = json.loads(str(report.semester3).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester4":
                    sem = json.loads(str(report.semester4).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester5":
                    sem = json.loads(str(report.semester5).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester6":
                    sem = json.loads(str(report.semester6).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester7":
                    sem = json.loads(str(report.semester7).replace("\'", "\""))
                elif str(request.POST.get("semester")) == "semester8":
                    sem = json.loads(str(report.semester8).replace("\'", "\""))

            number_of_courses = len(sem)
            base_tuition = 17000

            if int(number_of_courses) == 0:
                p = ""
            else:
                p = int(base_tuition) + int(number_of_courses * 1000)

            return render(request, "home/tuition.html",
                          {'student': stu, 'semester': sem, 'tuition': p,
                           'username': request.POST.get("username"), 'password': request.POST.get("password")})

    if request.method == 'GET':
        return render(request, "homepage.html")
