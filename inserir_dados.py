import names 
import random as rand
from neo4j import GraphDatabase
from keys import URL, USERNAME, PASSWORD
# from pprint import pprint

# Conexão com o banco de dados Neo4j
driver = GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD))

num_de_pessoas = int(input("Insira o numero de pessoas para inserir no banco: "))
depart = [453, 654, 236, 735]
formado = [True, False]

def inserir(query, params):
    with driver.session() as session:
        try:
            session.run(query, params)
            # pprint(params)
            # print("Dado inserido!")
        except Exception as e:
            print(e)

def atualizar(query, params):
    with driver.session() as session:
        try:
            session.run(query, params)
            # pprint(params)
            # print("Dado atualizado!")
        except Exception as e:
            print(e)

def relacionar(no_a, id_a, relacao, id_b, no_alvo):
    query = """
    MATCH (a:%s {%s}), (b:%s {%s})
    CREATE (a)-[:%s]->(b);
    """%(no_a, id_a, no_alvo, id_b, relacao)
    with driver.session() as session:
        session.run(query)
    # pprint(query)
def delete_all():
    delete_query = "MATCH (n) DETACH DELETE n"
    with driver.session() as session:
        session.run(delete_query)
    # print("Dados deletados!")

# Deletar dados existentes
delete_all()

# Inserir departamentos
departamentos = [
    {"id": 453, "nome_departamento": "Computacao", "id_chefe_departamento": 0},
    {"id": 654, "nome_departamento": "Engenharia", "id_chefe_departamento": 0},
    {"id": 236, "nome_departamento": "Administracao", "id_chefe_departamento": 0},
    {"id": 735, "nome_departamento": "Economia", "id_chefe_departamento": 0},
]

for dep in departamentos:
    query = """
    CREATE (d:Departamento {id: $id, nome_departamento: $nome_departamento, id_chefe_departamento: $id_chefe_departamento})
    """
    params = dep
    inserir(query, params)

# Inserir cursos
cursos = [
    {"id": 0, "nome_curso": "Administração de Empresas"},
    {"id": 1, "nome_curso": "Gestão de Recursos Humanos"},
    {"id": 2, "nome_curso": "Engenharia Civil"},
    {"id": 3, "nome_curso": "Engenharia Elétrica"},
    {"id": 4, "nome_curso": "Ciência da Computação"},
    {"id": 5, "nome_curso": "Engenharia de Software"},
    {"id": 6, "nome_curso": "Economia"},
    {"id": 7, "nome_curso": "Finanças"}
]

for curso in cursos:
    query = """
    CREATE (c:Curso {id: $id, nome_curso: $nome_curso})
    """
    data = curso
    inserir(query, data)

# Inserir disciplinas
disciplinas = [
    {"id": 0, "nome_disciplina": "Comp. Sci.", "id_departamento": 453, "semestre": 4},
    {"id": 1, "nome_disciplina": "Finance", "id_departamento": 654, "semestre": 7},
    {"id": 2, "nome_disciplina": "Eng. eletrica", "id_departamento": 236, "semestre": 3},
    {"id": 3, "nome_disciplina": "Physics", "id_departamento": 735, "semestre": 4},
    {"id": 4, "nome_disciplina": "Desenvolvimento Web", "id_departamento": 453, "semestre": 4},
    {"id": 5, "nome_disciplina": "Mercado de Capitais", "id_departamento": 654, "semestre": 7},
    {"id": 6, "nome_disciplina": "Eletromagnetismo", "id_departamento": 236, "semestre": 3},
    {"id": 7, "nome_disciplina": "Astrofísica", "id_departamento": 735, "semestre": 4},
    {"id": 8, "nome_disciplina": "Gestão de Recursos Humanos", "id_departamento": 453, "semestre": 0},
    {"id": 9, "nome_disciplina": "Segurança da Informação", "id_departamento": 654, "semestre": 7},
    {"id": 10, "nome_disciplina": "Gestão de Riscos", "id_departamento": 236, "semestre": 3},
    {"id": 11, "nome_disciplina": "Energias Renováveis", "id_departamento": 735, "semestre": 4},
    {"id": 12, "nome_disciplina": "Mecânica Quântica", "id_departamento": 453, "semestre": 4},
    {"id": 13, "nome_disciplina": "Marketing Estratégico", "id_departamento": 654, "semestre": 7},
    {"id": 14, "nome_disciplina": "Big Data Analytics", "id_departamento": 236, "semestre": 3},
    {"id": 15, "nome_disciplina": "Derivativos Financeiros", "id_departamento": 735, "semestre": 7},
    {"id": 16, "nome_disciplina": "Eletrônica de Potência", "id_departamento": 453, "semestre": 3},
    {"id": 17, "nome_disciplina": "Física Nuclear", "id_departamento": 654, "semestre": 4},
    {"id": 18, "nome_disciplina": "Empreendedorismo", "id_departamento": 236, "semestre": 0},
    {"id": 19, "nome_disciplina": "Aprendizado de Máquina", "id_departamento": 735, "semestre": 4},
    {"id": 20, "nome_disciplina": "Finanças Corporativas", "id_departamento": 453, "semestre": 7},
    {"id": 21, "nome_disciplina": "Telecomunicações", "id_departamento": 654, "semestre": 5},
    {"id": 22, "nome_disciplina": "Óptica Avançada", "id_departamento": 236, "semestre": 3},
    {"id": 23, "nome_disciplina": "Gestão da Qualidade", "id_departamento": 735, "semestre": 0}
]


for disciplina in disciplinas:
    query = """
    CREATE (d:Disciplina {id: $id, nome_disciplina: $nome_disciplina, id_departamento: $id_departamento, semestre: $semestre})
    """
    data = disciplina
    inserir(query, data)
    relacionar("Disciplina", "id:"+str(data["id"]), "PERTENCE", "id:"+str(data["id_departamento"]), "Departamento")

# Inserir professores e alunos
for i in range(num_de_pessoas):
    professor_query = """
    CREATE (p:Professor {id: $id, nome: $nome, departamento: $departamento})
    """
    professor_params = {
        "id": i,
        "nome": names.get_full_name(),
        "departamento": str(depart[rand.randint(0, 3)])
    }
    inserir(professor_query, professor_params)

    aluno_query = """
    CREATE (a:Aluno {id: $id, nome: $nome, formado: $formado})
    """
    aluno_params = {
        "id": i,
        "nome": names.get_full_name(),
        "formado": formado[1]
    }
    inserir(aluno_query, aluno_params)

# Inserir histórico do professor
for i in range(num_de_pessoas):
    for h in range(1, 4):
        historico_professor_query = """
        CREATE (hp:HistoricoProfessor {id_professor: $id_professor, id_disciplina: $id_disciplina, semestre: $semestre, ano: $ano})
        """
        data = {
            "id_professor": i,
            "id_disciplina": rand.randint(0, len(disciplinas)-1),
            "semestre": rand.randint(1, 8),
            "ano": rand.randint(2000, 2024)
        }
        inserir(historico_professor_query, data)
    print("id_professor:"+str(i))
    relacionar('HistoricoProfessor', "id_professor:"+str(i), 'Historico_de', "id:"+str(i), "Professor")
    relacionar('Disciplina', "id:b.id_disciplina", 'Conteúdo', "id_professor:"+str(i), "HistoricoProfessor")

# Inserir grupo TCC
for i in range(round(0.2 * num_de_pessoas)):
    grupo_tcc_query = """
    CREATE (gt:GrupoTCC {id_grupo: $id_grupo, id_professor: $id_professor})
    """
    data = {
        "id_grupo": i,
        "id_professor": rand.randint(0, num_de_pessoas)
    }
    inserir(grupo_tcc_query, data)
    relacionar('Professor', "id:"+str(i), 'Faz_parte', "id_grupo:"+str(i),   "GrupoTCC")

# Inserir histórico do aluno
for i in range(num_de_pessoas):
    nota = rand.uniform(0, 10)
    curso = rand.randint(0, 7)
    data_inicial = rand.randint(2000, 2024)
    sem_inicial = rand.randint(1, 8)

    # Inserir na matriz curricular
    matriz_curricular_query = """
    CREATE (mc:MatrizCurricular {id_aluno: $id_aluno, id_curso: $id_curso, ano: $ano, semestre: $semestre})
    """
    data = {
        "id_aluno": i,
        "id_curso": curso,
        "ano": data_inicial,
        "semestre": 8
    }
    inserir(matriz_curricular_query, data)
    relacionar('MatrizCurricular', "id_aluno:"+str(i), 'Cursa', "id:"+str(i), "Aluno")
    relacionar('MatrizCurricular', "id_curso:"+str(curso), 'Cumpre', "id:"+str(curso), "Curso")

    
    semestre = 0
    for m in range(0,len(disciplinas)):
        semestre += 1
        historico_aluno_query = """
        CREATE (ha:HistoricoAluno {id_aluno: $id_aluno, id_disciplina: $id_disciplina, semestre: $semestre, ano: $ano, nota: $nota})
        """
        data = {
            "id_aluno": i,
            "id_disciplina": disciplinas[m]["id"],
            "semestre": semestre,
            "ano": data_inicial,
            "nota": round(nota, 2)
        }
        inserir(historico_aluno_query, data)
        data_inicial += 1


        # Atualizar estado de formado
        if nota >= 5 and sem_inicial == 8:
            grupo = rand.randint(0, round(0.2 * num_de_pessoas))
            atualizar("MATCH (a:Aluno) WHERE a.id = $id SET a.formado = true, a.grupo_tcc = $grupo_tcc", 
                    {"id": i, 
                    "grupo_tcc": grupo
                    })
            relacionar('Aluno', "id:"+str(i), '`Faz parte`', "id_grupo:"+str(grupo), "GrupoTCC")
            # relacionar
        else:
            atualizar("MATCH (a:Aluno) WHERE a.id = $id SET a.formado = false", 
                    {"id": i})
    relacionar('HistoricoAluno', "id_aluno:"+str(i), 'Pertence', "id:"+str(i), "Aluno")
    relacionar('Disciplina', "id:b.id_disciplina", 'Conteúdo', "id_aluno:"+str(i), "HistoricoAluno")

# Atualizar chefes de departamentos
for dep_id in depart:
    chefe = rand.randint(0, num_de_pessoas)
    atualizar("MATCH (d:Departamento) WHERE d.id = $id SET d.id_chefe_departamento = $id_chefe_departamento", 
              {"id": dep_id, "id_chefe_departamento": chefe })
    relacionar('Professor', "id:"+str(chefe), 'Chefe', "id:"+str(dep_id), "Departamento")

# Fechar a conexão com o Neo4j
driver.close()
