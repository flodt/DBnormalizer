#!/usr/bin/python
# -*- coding: utf8 -*-
import cgi
import cgitb; cgitb.enable()
import views
param = cgi.FieldStorage()

#this file contains some schemas appearing in the exercise sheets of the tum gdb course
#if no parameter is given, this script prints all schema keys as html list items. If parameter "schema" is given, the corresponding schema will be printed.

schemas = {}
#format: "[attributes];[dependency#1];...;[dependency#n]"
schemas["s0"] = "ABCDEF;B->DA;DEF->B;C->EA"
schemas["s1"] = "Name,Aufgabe,Max,Erzielt,ErzieltSumme,MaxSumme,KNote,Bonus,GNote;KNote,Bonus->GNote;Aufgabe->Max;ErzieltSumme->KNote;Name,Aufgabe->Erzielt;Name->ErzieltSumme,Bonus,GNote;->MaxSumme"
schemas["s2"] = "ABCDEF;A->BC;C->DA;E->ABC;F->CD;CD->BEF"
schemas["s3"] = "ABCDEFG;A->BC;DE->B;F->A;E->BF;A->DE;C->A"
schemas["s4"] = "ABCD;AB->>C;BC->>D;BA->CD;DA->B"
schemas["s5"] = "person,kindName,kindAlter,fahrradTyp,fahrradFarbe;person->>kindName,kindAlter;person->>fahrradTyp,fahrradFarbe;kindName->kindAlter"
schemas["s6"] = "ABCDEF;AB->CD;ABC->D;E->C;D->C;CDE->AB"
schemas["s7"] = "matrnr,name,semester,vorlnr,titel,sws,gelesenvon;matrnr->name,semester;vorlnr->titel,sws,gelesenvon"

def getSchemaIds():
	schema_ids = []
	for schema_id in schemas:
		schema_ids.append(schema_id)
	return sorted(schema_ids)

print """
"""
try:
	schema_id = param['schema'].value
	print schemas[schema_id]
except KeyError:
	predefindedSchemaIds = getSchemaIds()
	schemaList = ""
	for i, schemaId in enumerate(predefindedSchemaIds):
		schemaList = schemaList + "<li><a href=\"#\" onclick=\"setContent('"+str(schemaId)+"')\">"+views.addTooltipText("Schema "+str(i+1), "R("+schemas[schemaId].replace(";", "; ").replace(";", "):", 1))+"</a></li>"
	print schemaList
