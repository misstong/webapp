import yate
import athletemodel
import cgi
import os

form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value
#athlete_name="Sarah Sweeney"
print(yate.start_response())
print(yate.include_header(athlete_name+"'s timing"))
#print(yate.para(athlete_name+"'s timing"))
data=athletemodel.get_from_store()

athlete=data[athlete_name]
print(yate.u_list(sorted(set(athlete))[:3]))
print(yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py"}))#os.path.join(os.getcwd(),"index.html")
    