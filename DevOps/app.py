from fastapi            import     FastAPI
from database           import     engine,Base
from routers.alunos     import     alunos_router
from routers.cursos     import     cursos_router
from routers.matriculas import matriculas_router
Base.metadata.create_all            (bind=engine)
app =FastAPI(title      =  'Gestão Escolar API', 
             description='''
                            EndPoints API para gerenciar alunos, cursos e turmas, em instituição de ensino,
                            permitindo realizar diferentes operações em cada uma dessas entidades.
                         ''',
             version    =  '1.1.1')
app.include_router(    alunos_router, tags=[    'Alunos'])
app.include_router(    cursos_router, tags=[    'Cursos'])
app.include_router(matriculas_router, tags=['Matriculas'])
