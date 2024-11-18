// https://console-preview.neo4j.io/tools/query

// histórico escolar de qualquer aluno,
// retornando o código e nome da disciplina,
// semestre e ano que a disciplina foi cursada e nota final

MATCH (a:Aluno {id:2})<-[:Pertence]-(h:HistoricoAluno)<-[:Conteúdo]-(d:Disciplina)
RETURN a,h,d


// histórico de disciplinas ministradas
// por qualquer professor, com semestre e ano

MATCH (p:Professor {id:2})<-[:`Historico_de`]-(h:HistoricoProfessor)
RETURN p,h

//listar alunos que já se formaram (foram aprovados em
// todos os cursos de uma matriz curricular) em um determinado semestre de um ano

MATCH (p:Aluno {formado:TRUE})<-[:`Cursa`]-(m:MatrizCurricular)
RETURN p,m

// listar todos os professores que são chefes
// de departamento, junto com o nome do departamento

MATCH (p:Professor)-[:`Chefe`]->(d:Departamento)
RETURN p,d

// saber quais alunos formaram um grupo
// de TCC e qual professor foi o orientador

MATCH (p:Professor)-[:Faz_parte]->(g:GrupoTCC)<-[:`Faz parte`]-(a:Aluno)
RETURN p,g,a