import pandas as pd
import dash
import base64
import dash_core_components as dcc
import dash_html_components as html

from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from flask import Flask, render_template

from flask_mysqldb import MySQL 

external_stylesheets = [dbc.themes.BOOTSTRAP,] #'https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.server.config["MYSQL_HOST"] = "127.0.0.1"
app.server.config["MYSQL_USER"] = "tatianabellagio"
app.server.config["MYSQL_PASSWORD"] = "Aa123456!"
app.server.config["MYSQL_DB"] = "grs_datos"
mysql = MySQL(app.server)
#mysql.init_app(app.server)

image_filename = 'Logo_White.png' # replace with your own image



encoded_image = base64.b64encode(open(image_filename, 'rb').read())

trabajadores = ["Médico/a",
"Enfermero/a",
"Camillero/a",
"Personal de Limpieza",
"Diagnóstico por imágenes",
"Laboratorio",
"Seguridad",
"Personal que maneja la ropa",
"Personal de Cocina"]

centros_salud = pd.read_csv("nombre_centros.csv",header=None, index_col = 0)[1]

colors = {
    'background': '#9fd5d1',
    'text': '#686868'
}

style_letter = {'fontSize': 25,"marginTop": 13, "font-family": "Calibri",  'color': colors['text']}


body = dbc.Container([ 
dbc.Row(
            [
            html.H1(children = "Sistema de Gestión de Recursos", style = {"font-family" : "Calibri"})
            ], justify="center", align="center", className="h-50"
            )


],style={'textAlign': 'center',
         'color': colors['text'],
         "marginTop": 5}

)




app.layout = html.Div(style={'backgroundColor': colors['background']},

children = [

    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style = { 'height':'20%', 'width':'20%'}),
    
    ], style={'textAlign': 'center', }),

    html.Div([ body
    
    ]),


    html.Div([
        dbc.Row(
            [
                dbc.Col( html.H1("¿Qué rol ocupa en el establecimiento?", style= style_letter
                        ),width=6  ),

                dbc.Col(dcc.Dropdown(id = "rol_establecimiento", 
                                     options=[{'label':i, 'value': j} for i,j in zip (trabajadores,trabajadores)],
                                     value=''
                        ),width=6 , style = style_letter  ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col( html.H1("¿En qué Institución trabajas?", style= style_letter
                        ),width=6  ,  ),

                dbc.Col(dcc.Dropdown(id = "institucion_trabajo", 
                                    options=[{'label':i, 'value': j} for i,j in zip (centros_salud,centros_salud)],
                                    value=''
                        ),width=6 , style = style_letter  ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col( html.H1("¿Estás en contacto con pacientes sospechosos de COVID?", style= style_letter
                        ),width= 6 ,  ),

                dbc.Col(dcc.Dropdown(id = "contacto_sospechosos", 
                                        options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'},
                                            ],
                                        value=''
                        ),width=6 , style = style_letter  ),
            ]
        ),
                dbc.Row(
            [
                dbc.Col( html.H1("¿Tenés contacto con pacientes antes de que se determine su diagnóstico?", style= style_letter
                        ),width= 6 ,  ),

                dbc.Col(dcc.Dropdown(id = "contacto_prediagnostico",
                                    options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width=6 ,style = style_letter   ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Estás al tanto del equipamiento necesario para atender a pacientes sospechosos de COVID-19?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "equipamiento_nec", 
                    
                    options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width=6 ,style = style_letter   ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Qué cantidad de barbijos quirúrgicos recibís por día?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "barbijos", 
                    options=[{'label':i, 'value': j} for i,j in zip (range(1, 20),range(1, 20)) ],
                                        value=''
                        ),width=6 , style = style_letter  ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Qué cantidad de pares de guantes descartables recibís por día?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "guantes", 
                    options=[{'label':i, 'value': j} for i,j in zip (range(1, 20),range(1, 20)) ],
                                        value=''
                        ),width=6 , style = style_letter  ),
            ]
        ),

                dbc.Row(
            [ 
                dbc.Col( html.H1("¿Qué cantidad de batas o camisolines recibís por día?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "batas", 
                    options=[{'label':i, 'value': j} for i,j in zip (range(1, 20),range(1, 20)) ],
                                        value=''
                        ),width= 6 , style = style_letter  ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Recibís gafas o protección ocular?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "gafas", 
                    options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width=6 , style = style_letter  ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Recibís Barbijos N-95?", style= style_letter
                        ),width=6 , style = style_letter  ),

                dbc.Col(dcc.Dropdown(id = "barbijos_n95", 
                    options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width=6 ,  style = style_letter ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Recibís  fármacos necesarios para el tratamiento de pacientes con COVID 19?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "farmacos", 
                    options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width=6 ,  style = style_letter ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Si tu última respuesta fue no, cuál/es te faltan?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Input(id = "input_farmacos", type = "text"
    
                        ),width=6 , style = style_letter  ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Qué insumo necesitarías como prioritario que no estás recibiendo?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Input( id = "input_insumo_prioritario", type = "text"
                        ),width=6 , style = style_letter  ),
            ]
        ),

                dbc.Row(
            [
                dbc.Col( html.H1("¿Perteneces a algún grupo de riesgo (más de 60 años o enf. como cáncer, hipertensión, respiratoria crónica, diabetes o cardiovasculares)?", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "grupo_riesgo",
                    options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width= 6 , style = style_letter  ),
            ]
        ),



                dbc.Row(
            [
                dbc.Col( html.H1("¿Querés formar parte de esta iniciativa para mejorar la gestión de recursos e insumos de tu centro? Dejanos un contacto más abajo (correo o tel).", style= style_letter
                        ),width=6 ,  ),

                dbc.Col(dcc.Dropdown(id = "parte_iniciativa",
                                     options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'}
                                            ],
                                        value=''
                        ),width=6 , style = style_letter ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col( html.H1("CONTACTO", style= style_letter
                        ),width=6),
                dbc.Col(dcc.Input( id = "contacto", type = "text"
                        ),width=6 , style = style_letter ),
            ]
        ),


        html.Div(dbc.Button(id='submit-button-state', n_clicks=0, children='Enviar información',
                             outline=True, color="secondary",size="lg"),
         style={'margin-left': 450, "margin-top": 25 }),


        html.Div(id = "rta", 
        style = {'fontSize': 25,"marginTop": 13, "font-family": "Calibri",  'color': colors['text'], "margin-top": 30, "margin-left": 450})
    ], style = {"marginTop": 30, "margin-left": 30, "margin-right": 30})
])

@app.callback(
    Output('rta', 'children'),
    [Input("submit-button-state", "n_clicks")], 
    [State('rol_establecimiento', 'value'),
    State('institucion_trabajo', 'value'),
    State('contacto_sospechosos', 'value'),
    State('contacto_prediagnostico', 'value'),
    State('equipamiento_nec', 'value'),
    State('barbijos', 'value'),
    State('guantes', 'value'),
    State('batas', 'value'),
    State('gafas', 'value'),
    State('barbijos_n95', 'value'),
    State('farmacos', 'value'),
    State('input_farmacos', 'value'),
    State('input_insumo_prioritario', 'value'),
    State('grupo_riesgo', 'value'),
    State('parte_iniciativa', 'value'),
    State("contacto", "value")])

def cargo_tabla(n_clicks,rol_establecimiento,institucion_trabajo, contacto_sospechosos,contacto_prediagnostico,equipamiento_nec,barbijos,guantes,batas,gafas,barbijos_n95,farmacos,input_farmacos,input_insumo_prioritario,
grupo_riesgo,parte_iniciativa, contacto):
    if n_clicks == 0:
        raise PreventUpdate
        rta = ""
    else:
        cur = mysql.connection.cursor()
        cur.execute("""insert into trabajadores_centros_salud (rol_establecimiento, institucion_trabajo,contacto_sospechosos,
        contacto_prediagnostico,equipamiento_nec,barbijos,guantes,batas,gafas,barbijos_n95,farmacos,input_farmacos,
        input_insumo_prioritario,grupo_riesgo,parte_iniciativa, contacto) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s,
        %s, %s, %s,%s, %s, %s, %s)""",(rol_establecimiento,
         institucion_trabajo, contacto_sospechosos,contacto_prediagnostico,equipamiento_nec,barbijos,guantes,batas,gafas,
         barbijos_n95,farmacos,input_farmacos,input_insumo_prioritario,grupo_riesgo,parte_iniciativa, contacto))
        mysql.connection.commit()
        rta = "Gracias por responder!"
    return rta

if __name__ == '__main__':
    app.run_server(debug=True)
