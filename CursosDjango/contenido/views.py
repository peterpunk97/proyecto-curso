from django.shortcuts import render, HttpResponse

# Create your views here

menu="""
    <a href="/principal">principal</a>
    <a href="/cursos">cursos</a>
    <a href="/contacto">contacto</a>
"""


def principal(request):
    contenido="""<h1>Hola Bienvenido</h1>
    <p>Aquí encontrarás cursos de tecnología acuerdo a tus necesidades</p>"""
    return HttpResponse(menu + contenido)


def cursos(request):
    contenido="""<h1>lista de cursos</h1><br>
    <h2>Cursos disponibles:</h2>
    <br>
    <ul>
        <li>Base de datos</li>
        <li>Programación</li>
        <li>Etc.</li>
    </ul>"""
    return HttpResponse(menu + contenido)


def contacto(request):
    contenido="""<h1>Ponte en contacto con nosotros</h1>
    <form>
        <label>Nombre:</label><br>
        <input type="text"><br><br>
        <label>Correo Electrónico:</label><br>
        <input type="email"<br><br><br>
        <label>Selecciona un curso:</label><br>
        <select>
            <option>Curso de Base de Datos</option>
            <option>Curso de Programación</option>
            <option>Etc...</option>
        </select><br><br>
        <label>Comentarios:</label><br>
        <textarea type="text"></textarea><br><br>
        
        <button type="submit">Enviar</button>
    </form>"""
    return HttpResponse(menu + contenido)