class Project:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion


project1 = Project('Proyecto 01', 'Descripción del proyecto 01')
project2 = Project('Proyecto 02', 'Descripción del proyecto 02')
project3 = Project('Proyecto 03', 'Descripción del proyecto 03')

PROJECTS = [project1, project2, project3]