IAMSPE = {
    "id_conv": "iamspe",
    "usuario": "01andar",
    "senha": "3456",
    "numeroCarteira": "82375600",
    "nomeSolicitante": "DANIELLA VODOLA FORCINA",
    "numeroConselhoSolicitante": "145256",
    "nomeExecutante": "DANIELLA VODOLA FORCINA",
    "numeroConselhoExecutante": "145256"
}

orizon = {
    "id_conv": "orizon",
    "operadora": "afresp",
    "usuario": "WEBSERVIC1",
    "senha": "Hosp@1234",
    "numeroCarteira": "0071440752",
    "numeroConselhoProfissionalExecutante": "28420",
    "numeroConselhoProfissionalSolicitante": "28420",
    "nomeProfissionalSolicitante": "Jorge Mitre",
    "codigoOperadora": "384291",
    "codigoProcedimento": "84500743"
}

central_nacional = {
    "id_conv": "central-nacional",
    "usuario": "cnu.ana.calasso",
    "senha": "tuta5874",
    "numeroCarteira": "2555000275011",
    "codigoOperadora": "11000786",
    "nomeProfissionalSolicitante": "Jorge Mitre",
    "codigoProcedimento": "77998260"
}

sao_cristovao = {
    "id_conv": "sao-cristovao",
    "usuario": "HOSP",
    "senha": "hosp1234",
    "numeroCarteira": "005046790000000100",
    "guiaPrestador": "2895943",
    "nomeProfissional": "Jorge Mitre",
    "crm": "2842",
    "cbo": "225265"
}

albert_heinsten = {
    "id_conv": "albert-einsten",
    "usuario": "43022466000109",
    "senha": "43022466000109",
    "numeroCarteira": "01948010202200",
    "numeroConselho": "28420",
    "nomeProfissional": "Jorge Mitre",
    "cbo": "225265",
    "codProcedimento": "10101012"
}

seguros_unimed = {
    "id_conv": "seguros-unimed",
    "usuario": "p9941737",
    "senha": "hosp10",
    "numeroCarteira": "09941163283833101",
    "ddd": "11",
    "tel_celular": "963531899",
    "email": "lecambauva@yahoo.com.br",
    "tipoConsulta": "Primeira Consulta",
    "profissional": "Jorge mitre",
    "crm": "28420",
    "cbos": "225265"
}

golden_cross = {
    "id_conv": "golden_cross",
    "usuario": "43022466000109",
    "senha": "Gold1000",
    "numeroGuia": "11102",
    "numeroCarteira": "2245396101",
    "cnpj": "43.022.466/0001-09",
    "numeroConselho": "28420",
    "nomeProfissional": "Jorge Mitre",
    "cbos": "225265",
    "codProcedimento": "10101012"
}

notre_dame = {
    "id_conv": "notre-dame-intermedica",
    "usuario": "14825",
    "senha": "814:=6102",
    "numeroGuia": "2893220",
    "numeroCarteira": "9700299200001470000",
    "codigoProcedimento": "10101012"
}

assefaz = {
    "id_conv": "assefaz",
    "usuario": "58394420000180",
    "senha": "Fatura2121",
    "numGuiaPrestador": "00112",
    "numeroCarteira": "00010121000064843",
    "nomeProfissional": "JORGE MITRE",
    "tipoConselho": "CRM",
    "uf": "sp",
    "numeroConselho": "28420",
    "cbo": "225265",
    "codigoProcedimento": "10101012"
}

conv = [
    list(assefaz.keys()),
    list(IAMSPE.keys()),
    list(seguros_unimed.keys()),
    list(sao_cristovao.keys()),
    list(central_nacional.keys()),
    list(orizon.keys()),
    list(notre_dame.keys()),
    list(albert_heinsten.keys()),
    list(golden_cross.keys()),
]

lista_campos = []

for item in conv:
    for campo in item:
        lista_campos.append(campo)

print(lista_campos)
print(set(lista_campos))
