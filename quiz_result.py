#!/usr/bin/python3
import cgi, cgitb, os
cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage()
q1 = form.getvalue("q1")
q2 = form.getvalue("q2")
q3 = form.getvalue("q3")
q4 = form.getvalue("q4")
q5 = form.getvalue("q5")
q6 = form.getvalue("q6")
q7 = form.getvalue("q7")
q8 = form.getvalue("q8")
q9 = form.getvalue("q9")
q10 = form.getvalue("q10")
q11 = form.getvalue("q11")
q12 = form.getvalue("q12")
q13 = form.getvalue("q13")
q14 = form.getvalue("q14")
q15 = form.getvalue("q15")
q16 = form.getvalue("q16")
q17 = form.getvalue("q17")
q18 = form.getvalue("q18")



print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title>Results</title></head>')
print('<body>')

print('<h1>results</h1>')

score = 0

print('<p>You filled in the following data:<br/>')

print('ans1 %s <br/>' % q1)
if q1 == "ada":
    score += 1
print('ans2 %s <br/>' % q2)
if q2 == "difference":
    score += 1
print('ans3 %s <br/>' % q3)
if q3 == "2002":
    score += 1
print('ans4 %s <br/>' % q4)
if "first programmer" in q4.lower():
    score += 1
print('ans5 %s <br/>' % q5)
if q5 == "byron":
    score += 1
print('ans6 %s <br/>' % q6)
if q6 == "poet":
    score += 1
print('ans7 %s <br/>' % q7)
if q7 == "1940":
    score += 1
print('ans8 %s <br/>' % q8)
if q8 == "welchmann":
    score += 1
print('ans9 %s <br/>' % q9)
if "GCHQ" in q9.upper():
    score += 1
print('ans10 %s <br/>' % q10)
if q10 == "true":
    score += 1
print('ans11 %s <br/>' % q11)
if q11 == "curious":
    score += 1
print('ans12 %s <br/>' % q12)
if q12 == "vassar":
    score += 1
print('ans13 %s <br/>' % q13)
if q13 == "bug":
    score += 1
print('ans14 %s <br/>' % q14)
if "computers don't understand english" in q14.lower() or "computers do not understand english" in q14.lower():
    score += 1
print('ans15 %s <br/>' % q15)
if q15 == "cobol":
    score += 1
print('ans16 %s <br/>' % q16)
if q16 == "compiler":
    score += 1
print('ans17 %s <br/>' % q17)
if q17 == "teach":
    score += 1
print('ans18 %s <br/>' % q18)
if q18 == "nlp":
    score += 1
print('You scored %s/18.\n Well Done!'% score)

print('</body>')
print('</html>')
